from calc import app
from flask import Flask, render_template, url_for, request, flash, redirect, abort
import locale
from calc import Funcoes

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

@app.template_filter()
def formatacaomoeda(valor):
    valor = float(valor)
    valor = locale.currency(valor, grouping=True)
    return valor

@app.route('/')
def index():
    return render_template('index.html', segment='index')

@app.route('/horaextra', methods=['GET', 'POST'])
def horaextra():
    if request.method == "POST":
            # Inputs de formulário do Usuário
            salario_digitado = Funcoes.Valor(request.form['salario_digitado']).tratar()
            hrmensais = int(request.form['hrmensais'])
            qtdehenormal = Funcoes.Hora(request.form['qtdehenormal']).transformacao()
            porchenormal = float(request.form['porchenormal'])
            qtdehecem = Funcoes.Hora(request.form['qtdehecem']).transformacao()
            porchecem = float(request.form['porchecem'])
            dias_uteis = int(request.form['dias_uteis'])
            dom_fer = int(request.form['dom_fer'])
            # Fim dos Inputs
            # Chamada de funções para cálculos
            valor_hora_util = Funcoes.ValorHora(salario_digitado, hrmensais).calcular_valor_hora()
            valorheunitutil = Funcoes.HE(salario_digitado, valor_hora_util, porchenormal, porchecem, qtdehenormal, qtdehecem).HE_unit_util()
            valorheunitcem = Funcoes.HE(salario_digitado, valor_hora_util, porchenormal, porchecem, qtdehenormal, qtdehecem).HE_unit_cem()
            valorheutil = Funcoes.HE(salario_digitado, valor_hora_util, porchenormal, porchecem, qtdehenormal, qtdehecem).HE_util()
            valorhecem = Funcoes.HE(salario_digitado, valor_hora_util, porchenormal, porchecem, qtdehenormal, qtdehecem).HE_cem()
            valordsrutil = Funcoes.DSR(valorheutil, valorhecem, dias_uteis, dom_fer).DSR_util()
            valordsrcem = Funcoes.DSR(valorheutil, valorhecem, dias_uteis, dom_fer).DSR_cem()

            # Fim da chamada de funções
            return render_template('resultadohe.html',
                                    salario_digitado = salario_digitado,
                                    valorheunitutil = valorheunitutil,
                                    valorheunitcem = valorheunitcem,
                                    valorheutil = valorheutil,
                                    valorhecem = valorhecem,
                                    valordsrutil = valordsrutil,
                                    valordsrcem = valordsrcem,  
                                    segment='resultadohe'                             
                                )
    else:
        return render_template('horaextra.html', segment='horaextra')
    

@app.route('/documentacao')
def documentacao():
    return render_template('documentacao.html', segment='documentacao')

@app.route('/ferias')
def ferias():
    return render_template('ferias.html', segment='ferias')
    
@app.route('/calculadorasalario', methods=['GET', 'POST'])
def calculadorasalario():
    if request.method == "POST":
            # Inputs de formulário do Usuário
            salario_digitado = Funcoes.Valor(request.form['salario_digitado']).tratar()
            qtde_dependentes = int(request.form['qtde_dependentes'])
            pensao = Funcoes.Valor(request.form['pensao']).tratar()
            hrmensais = int(request.form['hrmensais'])
            qtdehenormal = Funcoes.Hora(request.form['qtdehenormal']).transformacao()
            porchenormal = float(request.form['porchenormal'])
            qtdehecem = Funcoes.Hora(request.form['qtdehecem']).transformacao()
            porchecem = float(request.form['porchecem'])
            outras_bonificacoes = Funcoes.Valor(request.form['outras_bonificacoes']).tratar()
            dias_uteis = int(request.form['dias_uteis'])
            dom_fer = int(request.form['dom_fer'])
            desconto_vr = Funcoes.Valor(request.form['desconto_vr']).tratar()
            recebe_vt = request.form['recebe_vt']
            quant_hn_normais = Funcoes.Hora(request.form['quant_hn_normais']).transformacao()
            quant_hn_extra_diasuteis = Funcoes.Hora(request.form['quant_hn_extra_diasuteis']).transformacao()
            quant_hn_extra_domfer = Funcoes.Hora(request.form['quant_hn_extra_domfer']).transformacao()
            # Fim dos Inputs
            # Chamada de funções para cálculos
            valor_hora_util = Funcoes.ValorHora(salario_digitado, hrmensais).calcular_valor_hora()
            valorheutil = Funcoes.HE(salario_digitado, valor_hora_util, porchenormal, porchecem, qtdehenormal, qtdehecem).HE_util()
            valorhecem = Funcoes.HE(salario_digitado, valor_hora_util, porchenormal, porchecem, qtdehenormal, qtdehecem).HE_cem()
            valordsrutil = Funcoes.DSR(valorheutil, valorhecem, dias_uteis, dom_fer).DSR_util()
            valordsrcem = Funcoes.DSR(valorheutil, valorhecem, dias_uteis, dom_fer).DSR_cem()
            valor_hr_noturna = Funcoes.HoraNoturnaDiasUteis(valor_hora_util, quant_hn_normais).Hora_noturna_util()
            valor_hn_extra_diasuteis = Funcoes.HoraNoturnaExtraUtil(valor_hora_util, porchenormal, quant_hn_extra_diasuteis).Hora_noturna_extrautil()
            valor_hn_extra_cem = Funcoes.HoraNoturnaExtraCem(valor_hora_util, porchecem, quant_hn_extra_domfer).Hora_noturna_extracem()
            valor_salario_bruto = Funcoes.SalarioBruto(salario_digitado, valorheutil, valorhecem, valordsrutil, valordsrcem, valor_hr_noturna, valor_hn_extra_diasuteis, valor_hn_extra_cem, outras_bonificacoes).calculo_salario_bruto()
            valor_dsr_noturno_diasuteis = Funcoes.DsrHoraNoturnaExtraUtil(valor_hr_noturna, dias_uteis, dom_fer).Dsr_hn_extrautil()
            valor_dsr_noturno_cem = Funcoes.DsrHoraNoturnaExtraCem(valor_hn_extra_cem, dias_uteis, dom_fer).Dsr_hn_extracem()
            desconto_vt = Funcoes.ValeTransporte(salario_digitado, recebe_vt).calculo_vt()
            inss = Funcoes.INSS(salario_digitado).calcular_inss()
            irrf = Funcoes.IRRF(valor_salario_bruto, inss, qtde_dependentes, pensao).calcular_irrf()
            salario_liquido = Funcoes.SalarioLiquido(valor_salario_bruto, irrf, inss, desconto_vt, desconto_vr, pensao).calculo_salario_liquido()
            # Fim da chamada de funções
            return render_template('resultado.html',
                                    salario_digitado = salario_digitado,
                                    valorheutil = valorheutil,
                                    valorhecem = valorhecem,
                                    valordsrutil = valordsrutil,
                                    valordsrcem = valordsrcem,
                                    valor_hr_noturna = valor_hr_noturna,
                                    valor_hn_extra_diasuteis = valor_hn_extra_diasuteis,
                                    valor_hn_extra_cem = valor_hn_extra_cem,
                                    valor_dsr_noturno_diasuteis = valor_dsr_noturno_diasuteis,
                                    valor_dsr_noturno_cem = valor_dsr_noturno_cem,
                                    valor_salario_bruto = valor_salario_bruto,
                                    inss = inss,
                                    somainss = sum(inss.values()),
                                    irrf = irrf,
                                    somairrf = sum(irrf.values()),
                                    desconto_vr = desconto_vr,
                                    desconto_vt = desconto_vt,
                                    salario_liquido = salario_liquido,  
                                    segment='resultado'                             
                                )
    else:
        return render_template('calculadorasalario.html', segment='calculadorasalario')
    
if __name__ == "__main__":
    app.run(debug=True)