import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

# melhor forma de executar
# pytest -v  --disable-warnings .\test_views.py

@pytest.mark.django_db
def test_login(client):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_bolsista_editar(client):
    url = reverse('editar_bolsistas')
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_bolsista_listar(client):
    url = reverse('listar_bolsistas')
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.xfail
@pytest.mark.django_db
def test_bolsista_deletar(client):
    url = reverse('deletar_bolsistas/9/')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.xfail
@pytest.mark.django_db
def test_bolsista_detalhes(client):
    url = reverse('detalhes_bolsistas/11/')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def testar_login_111(client):
    response = client.post("/login/", {"username":"111", "password":"1234"})
    assert response.status_code == 200
    response = client.get("/sistema/")
    assert response.status_code == 200

@pytest.mark.django_db
def testar_login_2():
    cliente = Client()
    response = cliente.post("/login/", {"username":"111", "password":"1234566"})
    assert response.status_code == 200
    response = cliente.get("/sistema/")
    assert response.status_code == 200