from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Aluno
from .forms import AlunoForm


def lista_alunos(request):
    alunos = Aluno.objects.all().order_by('-criado_em')
    return render(request, 'lista.html', {'alunos': alunos})


def aluno_create(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save()
            messages.success(request, f'Aluno {aluno.nome} criado com sucesso!')
            return redirect('lista_alunos')
    else:
        form = AlunoForm()

    return render(request, 'aluno_form.html', {
        'form': form,
        'titulo': 'Novo Aluno'
    })


def aluno_detail(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'aluno_detalhe.html', {'aluno': aluno})


def aluno_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            aluno = form.save()
            messages.success(request, f'Aluno {aluno.nome} atualizado com sucesso!')
            return redirect('aluno_detail', pk=aluno.pk)
    else:
        form = AlunoForm(instance=aluno)

    return render(request, 'aluno_form.html', {
        'form': form,
        'titulo': f'Editar {aluno.nome}'
    })


def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)

    if request.method == 'POST':
        nome_aluno = aluno.nome
        aluno.delete()
        messages.success(request, f'Aluno {nome_aluno} excluído com sucesso!')
        return redirect('lista_alunos')

    return render(request, 'aluno_confirm_delete.html', {'aluno': aluno})