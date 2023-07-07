from django.db import IntegrityError
from django.shortcuts import redirect, render
from .models import Usuario, tipoUsuario, despacho, pedido, producto
from .forms import UsuarioForm, tipoForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def index(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/Home2.0.html", context)


def papeleria(request):
    return render(request, "pages/Papeleria (1).html", {})


def velas(request):
    return render(request, "pages/Velas.html", {})


def accesorios(request):
    return render(request, "pages/Accesorios.html", {})


def estampados(request):
    return render(request, "pages/Estampados.html", {})


def carrito(request):
    return render(request, "pages/CarroDefinitivo (2).html", {})


def registro(request):
    return render(request, "pages/registro.html", {})


def crud(request):
    usuario = Usuario.objects.all()
    context = {"usuario": usuario}
    return render(request, "pages/user_list.html", context)


def mpa1(request):
    return render(request, "pages/MPA1.html", {})


def mpa2(request):
    return render(request, "pages/MPA2.html", {})


def mpa3(request):
    return render(request, "pages/MPA3.html", {})


def mpa4(request):
    return render(request, "pages/MPA4.html", {})


def mpa5(request):
    return render(request, "pages/MPA5.html", {})


def mpa6(request):
    return render(request, "pages/MPA6.html", {})


def mpe1(request):
    return render(request, "pages/MPE1.html", {})


def mpe2(request):
    return render(request, "pages/MPE2.html", {})


def mpe3(request):
    return render(request, "pages/MPE3.html", {})


def mpe4(request):
    return render(request, "pages/MPE4.html", {})


def mpe5(request):
    return render(request, "pages/MPE5.html", {})


def mpp1(request):
    return render(request, "pages/MPP1.html", {})


def mpp2(request):
    return render(request, "pages/MPP2.html", {})


def mpp3(request):
    return render(request, "pages/MPP3.html", {})


def mpp4(request):
    return render(request, "pages/MPP4.html", {})


def mpp5(request):
    return render(request, "pages/MPP5.html", {})


def mpp6(request):
    return render(request, "pages/MPP6.html", {})


def mpv1(request):
    return render(request, "pages/MPV1.html", {})


def mpv2(request):
    return render(request, "pages/MPV2.html", {})


def mpv3(request):
    return render(request, "pages/MPV3.html", {})


def mpv4(request):
    return render(request, "pages/MPV4.html", {})


def userAdd(request):
    if request.method != "POST":
        tipo = tipoUsuario.objects.all()
        context = {"tipo": tipo}
        return render(request, "pages/user_add.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fecha = request.POST["fecha"]
        tipo = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)
        objUsuario = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            appPaterno=appPaterno,
            appMaterno=appMaterno,
            fechaNacimiento=fecha,
            tipoUsuario=objTipo,
            correo=correo,
            telefono=telefono,
            activo=1,
        )
        objUsuario.save()
        context = {"mensaje": "OK Registrado Correctamente"}
        return render(request, "pages/user_add.html", context)


def despachoAdd(request):
    correo = request.POST["correo"]
    nombres = request.POST["nombres"]
    apellidos = request.POST["apellidos"]
    rut = request.POST["rut"]
    direccion = request.POST["direccion"]
    numero = request.POST["numero"]
    dpto = request.POST["dpto"]
    fechaE = request.POST["fechaE"]

    objDespacho = despacho.objects.create(
        correo=correo,
        nombres=nombres,
        apellidos=apellidos,
        rut=rut,
        direccion=direccion,
        numero=numero,
        dpto=dpto,
        fechaE=fechaE,
    )
    objDespacho.save()
    context = {"mensaje": "OK Registrado Correctamente"}
    return render(request, "pages/home2.0.html", context)

def pedidoAdd(request):
    ID_pedido = request.POST["ID_pedido"]
    cantidad = request.POST["cantidad"]

    objPedido = pedido.objects.create(
        ID_pedido =  ID_pedido,
        cantidad = cantidad,

    )
    objPedido.save()
    context = {"mensaje": "OK Registrado Correctamente"}
    return render(request, "pages/home2.0.html", context)


def userDel(request, pk):
    context = {}
    try:
        user = Usuario.objects.get(rut=pk)

        user.delete()
        usuarios = Usuario.objects.all()
        context = {"mensaje": "OK Registro eliminado", "usuario": usuarios}
        return render(request, "pages/user_list.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {"mensaje": "Error, Rut no encontrado...",
                   "usuario": usuarios}
        return render(request, "pages/user_list.html", context)


def userEdit(request, pk):
    if pk != "":
        user = Usuario.objects.get(rut=pk)
        tipo = tipoUsuario.objects.all()
        context = {"usuario": user, "tipo": tipo}
        return render(request, "pages/user_edit.html", context)
    else:
        context = {"mensaje": "Error, usuario no encontrado"}
        return render(request, "pages/user_list", context)


def userUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fecha = request.POST["fecha"]
        tipo = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)

        user = Usuario()
        user.rut = rut
        user.nombre = nombre
        user.appPaterno = appPaterno
        user.appMaterno = appMaterno
        user.fechaNacimiento = fecha
        user.tipoUsuario = objTipo
        user.correo = correo
        user.telefono = telefono
        user.activo = 1
        user.save()

        tipo = tipoUsuario.objects.all()
        context = {"mensaje": "OK Registro modificado",
                   "tipo": tipo, "usuario": user}

        return render(request, "pages/user_edit.html", context)
    else:
        usuarios = Usuario.objects.all()
        context = {"usuario": usuarios}
        return render(request, "pages/user_list.html", context)


def formAdd(request):
    form = UsuarioForm()
    context = {"form": form}
    return render(request, "pages/formAdd.html", context)


def juegos(request):
    context = {}
    return render(request, "pages/apiVideojuegos.html", context)


def crudTipo(request):
    tipos = tipoUsuario.objects.all()
    context = {"tipo": tipos}
    return render(request, "pages/tipo_list.html", context)


def tipoAdd(request):
    if request.method != "POST":
        tipo = tipoForm()
        context = {"tipo": tipo}
        return render(request, "pages/tipo_add.html", context)
    else:
        form = tipoForm(request.POST)
        if form.is_valid():
            form.save()

            form = tipoForm()

            context = {"mensaje": "OK Agregado con exito", "tipo": form}
            return render(request, "pages/tipo_add.html", context)


def tipoDel(request, pk):
    if pk != "":
        tipo = tipoUsuario.objects.get(idTipoUsuario=pk)
        tipo.delete()

        tipos = tipoUsuario.objects.all()
        context = {"mensaje": "OK Tipo Eliminado", "tipo": tipos}
        return render(request, "pages/tipo_list.html", context)


def tipoEdit(request, pk):
    try:
        tipo = tipoUsuario.objects.get(idTipoUsuario=pk)
        context = {}
        if request.method != "POST":
            form = tipoForm(instance=tipo)
            context = {"form": form}
            return render(request, "pages/tipo_edit.html", context)
        else:
            form = tipoForm(request.POST, instance=tipo)
            form.save()

            context = {"mensaje": "OK Modificado con exito", "form": form}
            return render(request, "pages/tipo_edit.html", context)
    except:
        tipos = tipoUsuario.objects.all()
        context = {"mensaje": "Error, Tipo no encontrado...", "tipo": tipos}
        return render(request, "pages/tipo_list.html", context)


def login(request):
    context = {}
    if request.method != "POST":
        return render(request, "pages/login.html", context)
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        # print(f"Usuario: {username} \t Contraseña: {password}")
        # Reemplazar 'jo.riquelmee' por dato de la BDD
        # usuario = Usuario.objects.get(correo=username)
        if username == "Mcsou" and password == "pass1234":
            request.session["nombreUsuario"] = username
            usuarios = Usuario.objects.all()
            context = {"usuario": usuarios}
            return render(request, "pages/Home2.0.html", context)
        else:
            context = {"mensaje": "Usuario y/o Contraseña erronea"}
            return render(request, "pages/login.html", context)


def logout(request):
    del request.session["nombreUsuario"]
    context = {"mensaje": "Usuario Desconectado"}
    return render(request, "pages/login.html", context)


#funcion para registrar clientes en la base de datos:
def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'pages/registro.html', {'form': form})
    elif request.method == 'POST':
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm-password', '')

        if password == confirm_password and password != '':
            try:
                user = User.objects.create_user(
                    username=request.POST.get('username', ''), password=password)
                user.save()
                return HttpResponse('Usuario creado exitosamente')
            except Exception as e:
                print(e)
                return HttpResponse('Error al crear el usuario')
        else:
            return HttpResponse('Las contraseñas no coinciden o están vacías')
    else:
        return redirect('login')
