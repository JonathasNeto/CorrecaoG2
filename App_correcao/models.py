from django.db import models
from django.contrib.auth.models import User

class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    descricao = models.TextField()

    def __str__(self):
        return str(self.placa)

class Cargo(models.Model):
    nome = models.CharField(max_length=20)
    eh_chefe = models.BooleanField(default=False)
    eh_motorista = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField(max_length=20)
    eh_transporte = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    matricula = models.IntegerField()

    def __str__(self):
        return self.nome

class Solicitacao(models.Model):
    solicitante = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    origem = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    data = models.DateField()

    def __str__(self):
        return self.destino

class Atendimento(models.Model):
    solicitacao = models.ForeignKey(Solicitacao,on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo,on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE,related_name='Atendente')




