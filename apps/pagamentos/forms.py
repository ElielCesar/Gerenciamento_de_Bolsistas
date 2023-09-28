from django import forms
from apps.pagamentos.models import Relatorio

class Cadastrar_Relatorio(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = ['bolsista', 'mes', 'ano', 'valor_bolsa', 'relatorio', 'situacao', 'comprovante_pagamento']

        widgets = {
            'bolsista': forms.Select(attrs={'class':'form-control'}),
            'mes': forms.Select(attrs={'class':'form-control'}),
            'ano': forms.Select(attrs={'class':'form-control'}),
            'valor_bolsa': forms.NumberInput(attrs={'class':'form-control'}),
            'relatorio': forms.FileInput(attrs={'class':'form-control'}),
            'situacao': forms.Select(attrs={'class':'form-control'}),
            'comprovante_pagamento': forms.FileInput(attrs={'class':'form-control'}),
        }

