from django.views.generic import FormView
from django .urls import reverse_lazy
from django .contrib import messages

from .models import Servico, Funcionario, Feature

from .forms import ContatoForm

class IndexViews(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(IndexViews, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionario'] = Funcionario.objects.order_by('?').all()
        context['feature1'] = Feature.objects.all()[:3]
        context['feature2'] = Feature.objects.all()[3:6]
        return context


    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexViews, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexViews, self).form_invalid(form, *args, **kwargs)

    