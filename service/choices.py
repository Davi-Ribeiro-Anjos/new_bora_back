from django.db import models


class STATUS_CHOICES(models.TextChoices):
    ABERTO = "ABERTO"
    ANDAMENTO = "ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    CANCELADO = "CANCELADO"


class DEPARTAMENTO_CHOICES(models.TextChoices):
    DIRETORIA = "DIRETORIA"
    FATURAMENTO = "FATURAMENTO"
    FINANCEIRO = "FINANCEIRO"
    RH = "RH"
    FISCAL = "FISCAL"
    MONITORAMENTO = "MONITORAMENTO"
    OPERACIONAL = "OPERACIONAL"
    FROTA = "FROTA"
    EXPEDICAO = "EXPEDICAO"
    COMERCIAL = "COMERCIAL"
    JURIDICO = "JURIDICO"
    DESENVOLVIMENTO = "DESENVOLVIMENTO"
    TI = "TI"
    FILIAIS = "FILIAIS"
    COMPRAS = "COMPRAS"
    DEFAULT = "NÃO INFORMADO"


class FORMA_PGT_CHOICES(models.TextChoices):
    A_VISTA = "A VISTA"
    PARCELADO_1X = "PARCELADO 1X"
    PARCELADO_2X = "PARCELADO 2X"
    PARCELADO_3X = "PARCELADO 3X"
    PARCELADO_4X = "PARCELADO 4X"
    PARCELADO_5X = "PARCELADO 5X"
    PARCELADO_6X = "PARCELADO 6X"
    PARCELADO_7X = "PARCELADO 7X"
    PARCELADO_8X = "PARCELADO 8X"
    PARCELADO_9X = "PARCELADO 9X"
    PARCELADO_10X = "PARCELADO 10X"
    PARCELADO_11X = "PARCELADO 11X"
    PARCELADO_12X = "PARCELADO 12X"
    DEFAULT = "NÃO INFORMADO"


class CATEGORIA_CHOICES(models.TextChoices):
    ALMOXARIFADO = "ALMOXARIFADO"
    COTACAO = "COTACAO"
    NOTA_FISCAL = "NOTA FISCAL"
    DEFAULT = "NÃO INFORMADO"
