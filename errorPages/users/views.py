from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import *
from .models import CustomUser
from .forms import CustomUserCreationForm


# Hacer las vistas del API_REST de usuarios
class UserViewSets(viewsets.ModelViewSet):
    # 3 variables
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer]

    # Si quieres agregar la parte de seguridad pon estas 2 variables
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # Que métodos va a proteger
    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "DELETE"]:
            return [IsAuthenticated()]
        return []
    
    def destroy(self, request, *args, **kwargs):
        # Obtener el usuario que se va a eliminar
        user = self.get_object()

        # Obtener el usuario logueado
        logged_in_user = request.user

        # Verificar si el usuario está tratando de eliminar su propia cuenta
        if user == logged_in_user:
            # Generar una respuesta de error personalizada con el código de estado adecuado
            return Response(
                {"detail": "No puedes eliminar tu propio usuario."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Si no es el propio usuario, proceder con la eliminación
        return super().destroy(request, *args, **kwargs)


# Hacer una vista que me devuelva mi Token
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# Hacer una vista para el formulario de CustomUser
class CustomUserFormAPI(APIView):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        fields = {
            field: {
                "label": form[field].label,
                "input": form[field].field.widget.attrs,
                "type": form[field].field.widget.input_type,
            }
            for field in form.fields
        }
        return Response(fields)

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.data)
        if form.is_valid():
            user_data = form.cleaned_data
            User = get_user_model()
            user = User.objects.create_user(
                email=user_data["email"],
                password=user_data["password1"],
                name=user_data["name"],
                surname=user_data["surname"],
                control_number=user_data["control_number"],
                age=user_data["age"],
                tel=user_data["tel"],
            )
            return Response(
                {"message": "Usuario creado con éxito"}, status=status.HTTP_201_CREATED
            )
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
