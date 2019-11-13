from django import forms

from apps.preguntas.models import Encuesta

class PreguntasForm(forms.ModelForm):

    class Meta:
        model = Encuesta

        fields=[
            'name_user',
            'age',
            'pregunta_1',
            'pregunta_2',
            'pregunta_3',
            'pregunta_4',
            'pregunta_5',
        ]

        labels={
            'name_user' : 'Nombre', 
            'age' : 'Edad', 
            'pregunta_1' : 'Pregunta #1: Animal preferido.',
            'pregunta_2' : 'Pregunta #2: Comida favorita.',
            'pregunta_3' : 'Pregunta #3: Pais recomendado para visitar.',
            'pregunta_4' : 'Pregunta #4: Coche preferido.',
            'pregunta_5' : 'Pregunta #5: Marca de celulares recomendada.' ,
        }

        widgets ={
            'name_user': forms.TextInput(attrs={'class':'form-control'}),
            'age' : forms.TextInput(attrs={'class':'form-control'}),
            'pregunta_1': forms.TextInput(attrs={'class':'form-control'}),
            'pregunta_2': forms.TextInput(attrs={'class':'form-control'}),
            'pregunta_3': forms.TextInput(attrs={'class':'form-control'}),
            'pregunta_4': forms.TextInput(attrs={'class':'form-control'}),
            'pregunta_5': forms.TextInput(attrs={'class':'form-control'}),
        }
