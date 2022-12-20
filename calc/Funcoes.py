# Classe para tratar horas em cálculos
class Hora():
    def __init__(self, hora):
        self.hora = hora
        
    def transformacao(self):
        hora, minuto = self.hora.split(":")
        hora = float(hora)
        minuto = float(minuto)
        minuto = minuto/60
        quant_hora = hora + minuto
        return quant_hora

# Classe para tratar string dos valores com Input Mask
class Valor():
    def __init__(self, valor):
        self.valor = valor
        
    def tratar(self):
        valor_tratado = self.valor.replace('R$','')
        valor_tratado = valor_tratado.replace(' ','')
        valor_tratado = valor_tratado.replace('.','')
        valor_tratado = valor_tratado.replace(',','.')
        return float(valor_tratado)

# Classe que calcula o INSS  
class INSS():
    
    def __init__(self, salario):
        self.salario = salario
        self.primeira_faixa = 1212
        self.segunda_faixa = 2427.35
        self.terceira_faixa = 3641.03
        self.porc_desc_primeira = 7.5 / 100
        self.porc_desc_segunda = 9 / 100
        self.porc_desc_terceira = 12 / 100
        self.porc_desc_quarta = 14 / 100
        self.lista_inss = {}
        
    def calcular_inss(self):
        if self.salario < self.primeira_faixa:
            desc_primeira_faixa = self.salario * self.porc_desc_primeira
            print(f'O desconto da primeira faixa do INSS é de: R$ %.2f' %(desc_primeira_faixa))
            self.lista_inss[1] = desc_primeira_faixa
            # notas[nome] = nota
            return self.lista_inss
            
        else:
            if self.salario > self.primeira_faixa and self.salario <= self.segunda_faixa:
                desc_primeira_faixa = self.primeira_faixa * self.porc_desc_primeira
                desc_segunda_faixa = (self.salario - self.primeira_faixa)  * self.porc_desc_segunda
                self.lista_inss[1] = desc_primeira_faixa
                self.lista_inss[2] = desc_segunda_faixa
                return self.lista_inss
                
            elif self.salario > self.segunda_faixa and self.salario <= self.terceira_faixa:
                desc_primeira_faixa = self.primeira_faixa * self.porc_desc_primeira
                desc_segunda_faixa = (self.segunda_faixa - self.primeira_faixa)  * self.porc_desc_segunda
                desc_terceira_faixa = (self.salario - self.segunda_faixa)  * self.porc_desc_terceira
                self.lista_inss[1] = desc_primeira_faixa
                self.lista_inss[2] = desc_segunda_faixa
                self.lista_inss[3] = desc_terceira_faixa
                return self.lista_inss

            elif self.salario > self.terceira_faixa:
                desc_primeira_faixa = self.primeira_faixa * self.porc_desc_primeira
                desc_segunda_faixa = (self.segunda_faixa - self.primeira_faixa)  * self.porc_desc_segunda
                desc_terceira_faixa = (self.terceira_faixa - self.segunda_faixa)  * self.porc_desc_terceira
                desc_quarta_faixa = (self.salario - self.terceira_faixa)  * self.porc_desc_quarta
                self.lista_inss[1] = desc_primeira_faixa
                self.lista_inss[2] = desc_segunda_faixa
                self.lista_inss[3] = desc_terceira_faixa
                self.lista_inss[4] = desc_quarta_faixa
                return self.lista_inss

# Classe que calcula o valor da hora normal     
class ValorHora:
    def __init__(self, salario, hrmensais):
        self.salario = salario
        self.hrmensais = hrmensais
        
    def calcular_valor_hora(self):
        try:
            valor_hora = self.salario / self.hrmensais
            return valor_hora
        except ZeroDivisionError:
            return 0

# Classe que calcula o valor do desconto do imposto de renda
# Falta editar referente a base de calcula precisa ajustar para que seja o salario com todos acrescimos              
class IRRF:
    
    def __init__(self, valor_salario_bruto, inss, qtde_dependentes, pensao):
        self.valor_salario_bruto = valor_salario_bruto
        self.qtde_dependentes = qtde_dependentes
        self.inss = sum(inss)
        self.pensao = pensao
        self.primeira_faixa = 1903.99
        self.segunda_faixa = 2826.66
        self.terceira_faixa = 3751.06
        self.quarta_faixa = 4664.68
        self.deducao_dependente = 189.59
        
    def calcular_irrf(self):
        self.base_calculo = self.valor_salario_bruto - self.inss - (self.qtde_dependentes * self.deducao_dependente) - self.pensao
        desconto_irrf = {}
        
        if self.base_calculo < self.primeira_faixa:
            desconto_irrf = 0
            return desconto_irrf
        
        else:
            if self.base_calculo > self.primeira_faixa and self.base_calculo < self.segunda_faixa:
                valor_desconto_irrf_primeira = 0
                valor_desconto_irrf_segunda = (self.base_calculo - self.primeira_faixa) * 0.075
                desconto_irrf[1] = valor_desconto_irrf_primeira
                desconto_irrf[2] = valor_desconto_irrf_segunda
                #self.lista_inss[1] = desc_primeira_faixa
                return desconto_irrf
            
            elif self.base_calculo > self.segunda_faixa and self.base_calculo < self.terceira_faixa:
                valor_desconto_irrf_primeira = 0
                valor_desconto_irrf_segunda = (self.segunda_faixa - self.primeira_faixa) * 0.075
                valor_desconto_irrf_terceira = (self.base_calculo - self.segunda_faixa) * 0.15
                desconto_irrf[1] = valor_desconto_irrf_primeira
                desconto_irrf[2] = valor_desconto_irrf_segunda
                desconto_irrf[3] = valor_desconto_irrf_terceira
                return desconto_irrf
            
            elif self.base_calculo > self.terceira_faixa and self.base_calculo < self.quarta_faixa:
                valor_desconto_irrf_primeira = 0
                valor_desconto_irrf_segunda = (self.segunda_faixa - self.primeira_faixa) * 0.075
                valor_desconto_irrf_terceira = (self.terceira_faixa - self.segunda_faixa) * 0.15
                valor_desconto_irrf_quarta = (self.base_calculo - self.terceira_faixa) * 0.225
                desconto_irrf[1] = valor_desconto_irrf_primeira
                desconto_irrf[2] = valor_desconto_irrf_segunda
                desconto_irrf[3] = valor_desconto_irrf_terceira
                desconto_irrf[4] = valor_desconto_irrf_quarta
                return desconto_irrf 
        
            elif self.base_calculo > self.quarta_faixa:
                valor_desconto_irrf_primeira = 0
                valor_desconto_irrf_segunda = (self.segunda_faixa - self.primeira_faixa) * 0.075
                valor_desconto_irrf_terceira = (self.terceira_faixa - self.segunda_faixa) * 0.15
                valor_desconto_irrf_quarta = (self.quarta_faixa - self.terceira_faixa) * 0.225
                valor_desconto_irrf_quinta = (self.base_calculo - self.quarta_faixa) * 0.275
                desconto_irrf[1] = valor_desconto_irrf_primeira
                desconto_irrf[2] = valor_desconto_irrf_segunda
                desconto_irrf[3] = valor_desconto_irrf_terceira
                desconto_irrf[4] = valor_desconto_irrf_quarta
                desconto_irrf[5] = valor_desconto_irrf_quinta
                return desconto_irrf 

# Classe que calcula o valor da hora extra em dias úteis e domingos e feriados      
class HE:
    
    def __init__(self, salario, valor_hora_util, porchenormal, porchecem, qtdehenormal, qtdehecem):
        self.salario = salario
        self.valor_hora_util = valor_hora_util
        self.porchenormal = porchenormal / 100
        self.porchecem = porchecem / 100
        self.qtdehenormal = qtdehenormal
        self.qtdehecem = qtdehecem
        
    def HE_unit_util(self):
        valorheunitutil = float(self.valor_hora_util * (self.porchenormal + 1 ))
        return valorheunitutil
    
    def HE_unit_cem(self):
        valorheunitcem = float(self.valor_hora_util * (self.porchecem + 1 ))
        return valorheunitcem
    
    def HE_util(self):
        valorheutil = float(self.valor_hora_util * (self.porchenormal + 1 )) * self.qtdehenormal
        return valorheutil
    
    def HE_cem(self):
        valorhecem = float(self.valor_hora_util * (self.porchecem + 1 )) * self.qtdehecem
        return valorhecem

# Classe que calcula o valor do DSR em dias úteis e domingos e feriados     
class DSR:
    
    def __init__(self, valorheutil, valorhecem, dias_uteis, dom_fer):
        self.valorheutil = valorheutil
        self.valorhecem = valorhecem
        self.dias_uteis = dias_uteis
        self.dom_fer = dom_fer
        
    def DSR_util(self):
        dsrutil = float(self.valorheutil / self.dias_uteis) * self.dom_fer
        return dsrutil
        
    def DSR_cem(self):
        dsrcem = float(self.valorhecem / self.dias_uteis) * self.dom_fer
        return dsrcem
    
# Classe que calcula o valor da Hora noturna, sendo normal, extra em dias úteis ou em domingos e feriados
class HoraNoturnaDiasUteis:
    def __init__(self, valor_hora_util, quant_hn_extra_diasuteis):
        self.valor_hora_util = valor_hora_util
        self.quant_hn_extra_diasuteis = quant_hn_extra_diasuteis
        
    def Hora_noturna_util(self):
        valor_hr_noturna = float(self.valor_hora_util * 0.20) * self.quant_hn_extra_diasuteis
        return valor_hr_noturna
    
class HoraNoturnaExtraUtil:
    def __init__(self, valor_hora_util, porchenormal, quant_hn_extra_diasuteis):
        self.valor_hora_util = valor_hora_util
        self.porchenormal = porchenormal / 100
        self.quant_hn_extra_diasuteis = quant_hn_extra_diasuteis
        
    def Hora_noturna_extrautil(self):
        valor_hr_noturna_diasuteis = float(self.valor_hora_util * (0.20 + self.porchenormal)) * self.quant_hn_extra_diasuteis
        return valor_hr_noturna_diasuteis
    
class HoraNoturnaExtraCem:
    def __init__(self, valor_hora_util, porchecem, quant_hn_extra_domfer):
        self.valor_hora_util = valor_hora_util
        self.porchecem = porchecem / 100
        self.quant_hn_extra_domfer = quant_hn_extra_domfer
        
    def Hora_noturna_extracem(self):
        valor_hr_noturna_cem = float(self.valor_hora_util * (0.20 + self.porchecem)) * self.quant_hn_extra_domfer
        return valor_hr_noturna_cem
    
class DsrHoraNoturnaExtraUtil:
    def __init__(self, valor_hr_noturna_diasuteis, dias_uteis, dom_fer):
        self.valor_hr_noturna_diasuteis = valor_hr_noturna_diasuteis
        self.dias_uteis = dias_uteis
        self.dom_fer = dom_fer
    
    def Dsr_hn_extrautil(self):
        valor_dsr_noturno_diasuteis = (self.valor_hr_noturna_diasuteis / self.dias_uteis) * self.dom_fer
        return valor_dsr_noturno_diasuteis
    
class DsrHoraNoturnaExtraCem:
    def __init__(self, valor_hr_noturna_cem, dias_uteis, dom_fer):
        self.valor_hr_noturna_cem = valor_hr_noturna_cem
        self.dias_uteis = dias_uteis
        self.dom_fer = dom_fer
        
    def Dsr_hn_extracem(self):
        valor_dsr_noturno_cem = (self.valor_hr_noturna_cem / self.dias_uteis) * self.dom_fer
        return valor_dsr_noturno_cem

class ValeTransporte:
    
    def __init__(self, salario, recebe_vt):
        self.salario = salario
        self.recebe_vt = recebe_vt
    
    def calculo_vt(self):
        if self.recebe_vt == "S":
            desconto_vt = self.salario * 0.06
            return desconto_vt

        elif self.recebe_vt == "N":
            desconto_vt = 0
            return desconto_vt
            
class SalarioBruto:
    
    def __init__(self, salario, valorheutil, valorhecem, valordsrutil, valordsrcem, valor_hr_noturna, valor_hn_extra_diasuteis, valor_hn_extra_cem, outras_bonificacoes):
        self.salario = salario
        self.valorheutil = valorheutil
        self.valorhecem = valorhecem
        self.valordsrutil = valordsrutil
        self.valordsrcem = valordsrcem
        self.valor_hr_noturna = valor_hr_noturna
        self.valor_hn_extra_diasuteis = valor_hn_extra_diasuteis
        self.valor_hn_extra_cem = valor_hn_extra_cem
        self.outras_bonificacoes = outras_bonificacoes
    
    def calculo_salario_bruto(self):
        salario_bruto = self.salario + self.valorheutil + self.valorhecem + self.valordsrutil + self.valordsrcem + self.valor_hr_noturna + self.valor_hn_extra_diasuteis + self.valor_hn_extra_cem + self.outras_bonificacoes
        return salario_bruto
        
class SalarioLiquido:
    def __init__(self, salario_bruto, somairrf, somainss, desconto_vt, desconto_vr, pensao):
        self.salario_bruto = salario_bruto
        self.irrf = somairrf
        self.inss = somainss
        self.desconto_vt = desconto_vt
        self.desconto_vr = desconto_vr
        self.pensao = pensao
    
    def calculo_salario_liquido(self):
        salario_liquido = self.salario_bruto - self.irrf - self.inss - self.desconto_vt - self.desconto_vr - self.pensao
        return salario_liquido
    
    


class TercoFerias:
    def __init__(self, salario, media_proventos):
        self.salario = salario
        self.media_proventos = media_proventos
        
    def terco_ferias(self):
        terco_ferias = (self.salario + self.media_proventos) / 3
        return terco_ferias


class BaseFerias:
    def __init__(self, salario, media_proventos, terco_ferias):
        self.salario = salario
        self.media_proventos = media_proventos
        self.terco_ferias = terco_ferias
        
    def base_ferias(self):
        base_ferias = (self.salario + self.media_proventos + self.  terco_ferias)
        return base_ferias

class ValorFerias:
    def __init__(self, base_ferias, inss, irrf):
        self.base_ferias = base_ferias
        self.inss = inss
        self.irrf = irrf
    
    def valor_ferias(self):
        irrf = self.irrf
        inss = self.inss
        valor_ferias = self.base_ferias - inss - irrf
        return valor_ferias
    