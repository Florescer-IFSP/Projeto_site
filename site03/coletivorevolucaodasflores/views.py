from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from .models import Conteudo, Evento
from django.core.paginator import Paginator
from datetime import datetime
import os

MES = datetime.now().month
ANO = datetime.now().year

# Create your views here.
def home(request):
    eventos = Conteudo.objects.order_by('-data_publicacao')[:4]
    
    eventos_do_mes = Evento.objects.filter(data__year=ANO, data__month=MES)
    
    context = {'eventos': eventos,
            'eventos_do_mes': eventos_do_mes}
    
    # tambem fazer a interação quando clical no botao para avançar no calendario
    return render(request, 'home.html', context)



def obter_eventos_por_mes_ano(request):
    mes = request.GET.get('mes')
    ano = request.GET.get('ano')
    eventos = Evento.objects.filter(data__month=mes, data__year=ano)

    eventos_list = []
    for evento in eventos:
        eventos_list.append({
            'titulo': evento.evento,
            'local': evento.local,
            'data': evento.data.strftime('%d'),
            # Adicione mais campos conforme necessário
        })

    return JsonResponse(eventos_list, safe=False)

def eventos(request):
    # pegando os eventos não destacados do banco de dados para a exibição
    eventos_nao_destacados = Conteudo.objects.filter(destaque=False).order_by('-data_publicacao')
    # buscando pegar somente 10 noticas para exibir na tela
    paginator = Paginator(eventos_nao_destacados,8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if(page_number == None):
        page_number = 1
    #separar noticias sendo  5 noticias por partes
    noticias = len(eventos_nao_destacados)-((int(page_number)-1)*8)
    if noticias <= 4:
        eventos10 = page_obj[:4]
        eventos5 = page_obj[4:]
    else:
        eventos5 = page_obj[:4]
        eventos10 = page_obj[4:]
    # pegando as noticias destaque para por no site
    eventos_destacados = Conteudo.objects.filter(destaque=True).order_by('-data_publicacao')
    
    context = {'eventosD': eventos_destacados,
               'page_obj': page_obj,
               'eventosND5': eventos5,
               'eventosND10': eventos10}
    return render(request, 'pesquisa.html', context)

def visualizar_evento(request, id):
    evento = get_object_or_404(Conteudo, pk=id)
    return render(request, 'aba_pesquisa.html', {'evento': evento})

def projetos(request):
    return render(request, 'projetos.html')

def dowload_cartilha(request):
    pdf_path = os.path.join(settings.BASE_DIR,'templates', 'static', 'pdfs', 'Cartilha_Ecofeminismo.pdf')
    
    with open(pdf_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Cartilha_Ecofeminismo.pdf"'
        return response

def sobre(request):
    return render(request, 'sobre.html')

def doacao(request):
    return render(request, 'doacao.html')