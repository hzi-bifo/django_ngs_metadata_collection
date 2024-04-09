from django import forms
import json
import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic import ListView
from funky_sheets.formsets import HotView
from django.forms import CheckboxSelectMultiple, CheckboxInput, DateInput, modelformset_factory
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from .mixs_metadata_standards import MIXS_METADATA_STANDARDS
from .forms import OrderForm, SampleForm, SampleMetadataForm
from .models import Order, Sample, STATUS_CHOICES

logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('order_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        orders = Order.objects.filter(user=self.request.user)
        for order in orders:
            order.mixs_standards = order.sample_set.values_list('mixs_metadata_standard', flat=True).distinct()
        return orders

def order_view(request, order_id=None):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                # Process the form data and save the order
                # You can access the form data using form.cleaned_data
                # For example:
                # name = form.cleaned_data['name']
                # billing_address = form.cleaned_data['billing_address']
                # ag_and_hzi = form.cleaned_data['ag_and_hzi']
                # Create a new Order instance and save it
                order = Order(user=request.user)
                order.save()
                return redirect('order_list')
        else:
            form = OrderForm()

        return render(request, 'order_form.html', {'form': form})
    else:
        return redirect('login')

def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    order.delete()
    return redirect('order_list')   

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('order_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def samples_view(request, order_id):
    print("Received POST request")
    order = get_object_or_404(Order, pk=order_id)

    if request.method == 'POST':
        sample_data = json.loads(request.POST.get('sample_data'))
        print(f"Received sample_data: {sample_data}")

         # Delete all existing samples for the order
        Sample.objects.filter(order=order).delete()

        # Create new samples based on the received data
        for sample_info in sample_data:
            index = sample_info.get('index')
            concentration = sample_info.get('concentration')
            sample_name = sample_info.get('sample_name')
            volume = sample_info.get('volume')
            ratio_260_280 = sample_info.get('ratio_260_280')
            ratio_260_230 = sample_info.get('ratio_260_230')
            comments = sample_info.get('comments')
            mixs_metadata_standard = sample_info.get('mixs_metadata_standard', '')
            status = sample_info.get('status', '')

            print(f"Processing sample {index} with concentration {concentration}, volume {volume}, ratio_260_280 {ratio_260_280}, ratio_260_230 {ratio_260_230}, comments {comments}, mixs_metadata_standard {mixs_metadata_standard}, status {status}")

            sample = Sample(
                order=order,
                sample_name=sample_name,
                concentration=concentration,
                volume=volume,
                ratio_260_280=ratio_260_280,
                ratio_260_230=ratio_260_230,
                comments=comments,
                mixs_metadata_standard=mixs_metadata_standard,
                status=status
                
            )
            if status:
                sample.status = status  # Set the status field only if it's not an empty string

            sample.save()
            

        return JsonResponse({'success': True})

    samples = order.sample_set.all().order_by('sample_name')
    print(f"Retrieved samples: {list(samples)}")
    samples_data = [
        {
            'index': index,
            'sample_name': sample.sample_name or '',
            'mixs_metadata_standard': sample.mixs_metadata_standard or '',
            'concentration': sample.concentration or '',
            'volume': sample.volume or '',
            'ratio_260_280': sample.ratio_260_280 or '',
            'ratio_260_230': sample.ratio_260_230 or '',
            'comments': sample.comments or '',
            'status': sample.get_status_display() or ''
        }
        for index, sample in enumerate(samples, start=1)
    ]
    status_choices = [choice[1] for choice in STATUS_CHOICES]

    print(f"Sending samples_data to template: {samples_data}")
    return render(request, 'samples.html', {
            'order': order,
            'samples': samples_data,
            'mixs_metadata_standards': MIXS_METADATA_STANDARDS,
            'status_choices': status_choices,
        })

def mixs_view(request, order_id, mixs_standard):
    print(f"Received request for order_id: {order_id} with mixs_standard: {mixs_standard}")
    order = Order.objects.get(id=order_id)
    
    # Convert the mixs_standard to the format without whitespaces
    # Find the tuple in MIXS_METADATA_STANDARDS where the second element matches mixs_standard
    # and use the first element of that tuple as the mixs_metadata_standard
    mixs_metadata_standard = next((item[0] for item in MIXS_METADATA_STANDARDS if item[1] == mixs_standard), None)
    if not mixs_metadata_standard:
        return JsonResponse({'error': 'Invalid MIXS metadata standard'}, status=400)
    
    # Filter the samples based on the order and mixs_metadata_standard
    samples = Sample.objects.filter(order=order, mixs_metadata_standard=mixs_metadata_standard)
    print(f"Found {samples.count()} samples for order_id: {order_id}")

    if request.method == 'POST':
        try:
            mixs_metadata = json.loads(request.body)
            print(f"Received POST data: {mixs_metadata}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        for metadata in mixs_metadata:
            sample_id = metadata.get('sample_id')
            metadata_values = metadata.get('metadata')
            print(f"Processing metadata for sample_id: {sample_id}")
            try:
                sample = Sample.objects.get(id=sample_id)
                sample.mixs_metadata = metadata_values
                sample.save()
                print(f"Updated mixs_metadata for sample_id: {sample_id}")
            except Sample.DoesNotExist:
                print(f"Sample with id {sample_id} does not exist.")
                continue
        return JsonResponse({'success': True})
    else:
        initial_data = []
        for sample in samples:
            initial_data.append({
                'id': sample.id,
                'mixs_metadata': sample.mixs_metadata or {}
            })
        print(f"Preparing initial data for form: {initial_data}")
        form = SampleMetadataForm(mixs_metadata_standard=mixs_metadata_standard, initial=initial_data)

    context = {
        'order': order,
        'samples': samples,
        'form': form,
        'mixs_standard': mixs_standard, 
    }
    return render(request, 'mixs_view.html', context)
    
def order_list_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_list.html', {'orders': orders, 'user': request.user})

def order_view(request, order_id=None):
    if request.user.is_authenticated:
        if order_id:
            order = get_object_or_404(Order, pk=order_id, user=request.user)
            form = OrderForm(instance=order)
        else:
            form = OrderForm()

        if request.method == 'POST':
            if order_id:
                form = OrderForm(request.POST, instance=order)
            else:
                form = OrderForm(request.POST)

            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                return redirect('order_list')

        return render(request, 'order_form.html', {'form': form})
    else:
        return redirect('login')
