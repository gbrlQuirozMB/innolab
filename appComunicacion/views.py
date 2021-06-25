from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import permissions

from api.exceptions import *
from .serializers import *
from api.logger import log

from django.core.mail import send_mail


class EnviarCorreoCreateView(CreateAPIView):
    serializer_class = DatosCorreoSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = DatosCorreoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                nombre = request.data.get('nombre')
                telefono = request.data.get('telefono')
                email = request.data.get('email')
                servicioDeseado = request.data.get('servicioDeseado')
                nl = '\n'
                text_content = f'Hola,{nl}{nl} El cliente: {nombre}. {nl} Está solicitando se le agende una cita para: {servicioDeseado}. {nl} Datos de contacto: {nl} \t Teléfono: {telefono} {nl} \t Email: {email}'
                send_mail(
                    'INNOLAB - Solicitud cita',
                    text_content,
                    'no-reply@innolab.mx',
                    ['contacto@innolab.com.mx'],
                    fail_silently=False,
                )
            except:
                raise ResponseError(f'Error al enviar correo', 500)

            return self.create(request, *args, **kwargs)
        log.info(f'campos incorrectos: {serializer.errors}')
        raise ResponseBadRequest(serializer.errors)
