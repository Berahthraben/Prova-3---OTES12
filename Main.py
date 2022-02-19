import PySimpleGUI as sg
from DB import *
import os


def main():

    # ACESSO AO BANCO #

    senha = ''
    layout_temp = [[sg.Text("Favor inserir a senha do banco")],
                   [sg.Input("", key='senha')],
                   [sg.Button("Confirmar", key='confirmar')]]
    input_window = sg.Window('Inserir senha', layout_temp,
                             font='Arial 18',
                             element_justification='center',
                             auto_size_buttons=True,
                             auto_size_text=True)
    event, values = input_window.read()
    if event:
        senha = values['senha']
        input_window.close()
    else:
        input_window.close()
    banco = Database(senha)
    if not banco.connected:
        print("Erro em autenticar!")
        return

    # LAYOUT MAIN UI #

    layout_main = [[sg.Text("CONSULTAR")],
                   [sg.Button("Capacidade de Processos", key="consultar_capacidade"),
                    sg.Button("Volume", key='consultar_volume'),
                    sg.Button("SMI", key="consultar_SMI"),
                    sg.Button("Integridade", key="consultar_integridade"),
                    sg.Button("DRE", key="consultar_DRE"),
                    sg.Button("Exposição", key="consultar_exposicao")],
                   [sg.Text("INSERIR")],
                   [sg.Button("Capacidade de Processos", key="inserir_capacidade"),
                    sg.Button("Volume", key='inserir_volume'),
                    sg.Button("SMI", key="inserir_SMI"),
                    sg.Button("Integridade", key="inserir_integridade"),
                    sg.Button("DRE", key="inserir_DRE"),
                    sg.Button("Exposição", key="inserir_exposicao")],
                   [sg.Text("DELETAR")],
                   [sg.Button("Capacidade de Processos", key="deletar_capacidade"),
                    sg.Button("Volume", key='deletar_volume'),
                    sg.Button("SMI", key="deletar_SMI"),
                    sg.Button("Integridade", key="deletar_integridade"),
                    sg.Button("DRE", key="deletar_DRE"),
                    sg.Button("Exposição", key="deletar_exposicao")],
                   [sg.Text("ATUALIZAR")],
                   [sg.Button("Capacidade de Processos", key="atualizar_capacidade"),
                    sg.Button("Volume", key='atualizar_volume'),
                    sg.Button("SMI", key="atualizar_SMI"),
                    sg.Button("Integridade", key="atualizar_integridade"),
                    sg.Button("DRE", key="atualizar_DRE"),
                    sg.Button("Exposição", key="atualizar_exposicao")],
                   [sg.Button("Sair", key='sair')]]

    main_window = sg.Window('Prova 3 - Nicolas Ribeiro - OTES12', layout_main,
                             font='Arial 18',
                             element_justification='center',
                             auto_size_buttons=True,
                             auto_size_text=True)
    while(True):
        event, values = main_window.read()
        main_window.disable()
        main_window.hide()
        if event == "sair":
            main_window.close()
            return

        # CONSULTAR

        elif event == "consultar_capacidade":
            consultar(banco, "capacidade")
        elif event == "consultar_volume":
            consultar(banco, "volume")
        elif event == "consultar_SMI":
            consultar(banco, "SMI")
        elif event == "consultar_integridade":
            consultar(banco, "integridade")
        elif event == "consultar_DRE":
            consultar(banco, "DRE")
        elif event == "consultar_exposicao":
            consultar(banco, "exposicao")

        # ATUALIZAR #

        elif event == "atualizar_capacidade":
            atualizar(banco, "capacidade")
        elif event == "atualizar_volume":
            atualizar(banco, "volume")
        elif event == "atualizar_SMI":
            atualizar(banco, "SMI")
        elif event == "atualizar_integridade":
            atualizar(banco, "integridade")
        elif event == "atualizar_DRE":
            atualizar(banco, "DRE")
        elif event == "atualizar_exposicao":
            atualizar(banco, "exposicao")

        # INSERIR #


        elif event == "inserir_capacidade":
            inserir(banco, "capacidade")
        elif event == "inserir_volume":
            inserir(banco, "volume")
        elif event == "inserir_SMI":
            inserir(banco, "SMI")
        elif event == "inserir_integridade":
            inserir(banco, "integridade")
        elif event == "inserir_DRE":
            inserir(banco, "DRE")
        elif event == "inserir_exposicao":
            inserir(banco, "exposicao")

        # DELETAR #

        elif event == "deletar_capacidade":
            deletar(banco, "capacidade")
        elif event == "deletar_volume":
            deletar(banco, "volume")
        elif event == "deletar_SMI":
            deletar(banco, "SMI")
        elif event == "deletar_integridade":
            deletar(banco, "integridade")
        elif event == "deletar_DRE":
            deletar(banco, "DRE")
        elif event == "deletar_exposicao":
            deletar(banco, "exposicao")

        else:
            main_window.close()
            return
        main_window.enable()
        main_window.un_hide()



def inserir(banco, funcao):
    if funcao == "capacidade":
        niveis = ["1 - Processo possue resultados definidos",
                  "2 - A execução é planejada e monitorada",
                  "3 - Pessoas estão preparadas para realizar suas responsabilidades"]
        layout_temp = [[sg.Text("Selecione o Nivel do processo a ser inserido:")],
                       [sg.Combo(niveis, default_value=niveis[0], key='combo')],
                       [sg.Button("Confirmar", key='confirmar')]]
        window_temp = sg.Window('Selecionar nivel processo', layout_temp,
                             font='Arial 18',
                             element_justification='center',
                             auto_size_buttons=True,
                             auto_size_text=True)
        event, values = window_temp.read()
        if event == 'confirmar':
            window_temp.close()
            nivel = niveis.index(values['combo']) + 1
            window_temp.close()
            niveis_evidencia = [x + 1 for x in range(5)]
            layout_inserir = [[sg.Input("", key='texto'), sg.Combo(niveis_evidencia,
                                                                   default_value=niveis_evidencia[0],
                                                                   key='evidencia')],
                              [sg.Button("Confirmar", key='confirmar'), sg.Button("Cancelar")]]
            if nivel == 1:
                layout_inserir.insert(0, [sg.Text("O processo produz os resultados definidos | Fonte evidência")])
            elif nivel == 2:
                layout_inserir.insert(0, [sg.Text("A execução é planejada e monitorada | Fonte evidência")])
            elif nivel == 3:
                layout_inserir.insert(0, [sg.Text("Pessoas estão preparadas para realizar suas responsabilidades")])
            else:
                return
            window_inserir = sg.Window('Inserir processo', layout_inserir,
                                       font='Arial 18',
                                       element_justification='center',
                                       auto_size_buttons=True,
                                       auto_size_text=True)
            event, values = window_inserir.read()
            if event == 'confirmar':
                window_inserir.close()
                #print("Salvando!")
                #print(values['texto'])
                #print(values['nivel'])
                query = """
                INSERT INTO Capacidade (nivel, descricao, fonte) VALUES ({}, \'{}\', {});
                """.format(nivel, values['texto'], values['evidencia'])
                print(query)
                ret = banco.model_create_update(query, "")
                if ret == 0:
                    sg.Popup("Erro ao salvar!")
                else:
                    sg.Popup("Salvo com sucesso!")
                window_inserir.close()
            else:
                window_inserir.close()
                return
        else:
            window_temp.close()
            return
        window_temp.close()
    elif funcao == "volume":
        layout_inserir = [[sg.Text("n1"), sg.Input("", key='n1')],
                          [sg.Text("n2"), sg.Input("", key='n2')],
                          [sg.Text("N2"), sg.Input("", key='N2')],
                          [sg.Button("Confirmar", key='confirmar'), sg.Button("Cancelar")]]
        window_inserir = sg.Window('Inserir Volume', layout_inserir,
                                   font='Arial 18',
                                   element_justification='center',
                                   auto_size_buttons=True,
                                   auto_size_text=True)
        event, values = window_inserir.read()
        if event == 'confirmar':
            window_inserir.close()
            n1 = int(values['n1'])
            n2 = int(values['n2'])
            N2 = int(values['N2'])
            result = (2 / n1) * (n2 / N2)
            layout_confirmar = [[sg.Text("RESULTADO VOLUME MINIMO ALGORITMO")],
                                [sg.Text(str(result))],
                                [sg.Text("Gostaria de salvar o resultado?")],
                                [sg.Button("Confirmar", key='confirmar'), sg.Button("Cancelar", key='cancelar')]]
            window_confirmar = sg.Window('Confirmar inserção', layout_confirmar,
                                   font='Arial 18',
                                   element_justification='center',
                                   auto_size_buttons=True,
                                   auto_size_text=True)
            event, values = window_confirmar.read()
            if event == 'confirmar':
                #print("Salvando")
                #print("n1: {} | n2: {} | N2: {}".format(str(n1), str(n2), str(N2)))
                #print("Result: {}".format(result))
                query = """
                                INSERT INTO Volume (enep_1, enep_2, eneg_2, result) VALUES ({}, {}, {}, {});
                                """.format(n1, n2, N2, result)
                ret = banco.model_create_update(query, "")
                if ret == 0:
                    sg.Popup("Erro ao salvar!")
                else:
                    sg.Popup("Salvo com sucesso!")
                window_inserir.close()
            else:
                window_confirmar.close()
                return
            window_confirmar.close()
        else:
            window_inserir.close()
            return
        window_inserir.close()
    elif funcao == "SMI":
        layout_inserir = [[sg.Text("Mt"), sg.Input("", key='Mt')],
                          [sg.Text("Fc"), sg.Input("", key='Fc')],
                          [sg.Text("Fa"), sg.Input("", key='Fa')],
                          [sg.Text("Fd"), sg.Input("", key='Fd')],
                          [sg.Button("Confirmar", key='confirmar'), sg.Button("Cancelar")]]
        window_inserir = sg.Window('Inserir SMI', layout_inserir,
                                   font='Arial 18',
                                   element_justification='center',
                                   auto_size_buttons=True,
                                   auto_size_text=True)
        event, values = window_inserir.read()
        if event == 'confirmar':
            window_inserir.close()
            Mt = int(values['Mt'])
            Fc = int(values['Fc'])
            Fa = int(values['Fa'])
            Fd = int(values['Fd'])
            result = (Mt - (Fa + Fc + Fd)) / Mt
            layout_confirmar = [[sg.Text("RESULTADO SMI")],
                                [sg.Text(str(result))],
                                [sg.Text("Gostaria de salvar o resultado?")],
                                [sg.Button("Confirmar", key='confirmar'), sg.Button("Cancelar", key='cancelar')]]
            window_confirmar = sg.Window('Confirmar inserção', layout_confirmar,
                                         font='Arial 18',
                                         element_justification='center',
                                         auto_size_buttons=True,
                                         auto_size_text=True)
            event, values = window_confirmar.read()
            if event == 'confirmar':
                print("Salvando")
                print("Mt: {} | Fc: {} | Fa: {} | Fd: {}".format(str(Mt), str(Fc), str(Fa), str(Fd)))
                print("Result: {}".format(result))
                query = """INSERT INTO SMI (Mt, Fc, Fa, Fd, result) VALUES ({}, {}, {}, {}, {});
                """.format(Mt, Fc, Fa, Fd, result)
                ret = banco.model_create_update(query, "")
                if ret == 0:
                    sg.Popup("Erro ao salvar!")
                else:
                    sg.Popup("Salvo com sucesso!")
                window_inserir.close()
            else:
                window_confirmar.close()
                return
            window_confirmar.close()
        else:
            window_inserir.close()
            return
        window_inserir.close()
    elif funcao == "integridade":
        layout_inserir = [[sg.Text("Ameaça"), sg.Input("", key='ameaca')],
                          [sg.Text("Segurança"), sg.Input("", key='seguranca')],
                          [sg.Text("""
                          OBS: USE PONTO PARA DECIMAIS E INSIRA CADA DADO SEPARADO
                           POR VIRGULA PARA MAIS DE UMA ENTRADA""")],
                          [sg.Button("Confirmar", key='confirmar'), sg.Button("Cancelar")]]
        window_inserir = sg.Window('Inserir Integridade', layout_inserir,
                                   font='Arial 18',
                                   element_justification='center',
                                   auto_size_buttons=True,
                                   auto_size_text=True)
        event, values = window_inserir.read()
        if event == 'confirmar':
            window_inserir.close()
            ameaca = values['ameaca']
            seguranca = values['seguranca']
            ameaca_list = values['ameaca'].split(',')
            seguranca_list = values['seguranca'].split(',')
            if len(ameaca_list) != len(seguranca_list):
                sg.Popup("Erro! Ameaça e segurança tem tamanhos diferentes")
                window_inserir.close()
                return
            result = 0
            for i in range(len(ameaca_list)):
                result = result + (1 - (float(ameaca_list[i]) * (1 - float(seguranca_list[i]))))
            layout_confirmar = [[sg.Text("RESULTADO INTEGRIDADE")],
                                [sg.Text(str(result))],
                                [sg.Text("Gostaria de salvar o resultado?")],
                                [sg.Button("Confirmar", key='confirmar'), sg.Button("Cancelar", key='cancelar')]]
            window_confirmar = sg.Window('Confirmar inserção', layout_confirmar,
                                         font='Arial 18',
                                         element_justification='center',
                                         auto_size_buttons=True,
                                         auto_size_text=True)
            event, values = window_confirmar.read()
            if event == 'confirmar':
                print("Salvando")
                # print("ameaca: {} | seguranca: {}".format(str(ameaca), str(seguranca)))
                # print("Result: {}".format(result))
                query = """INSERT INTO Integridade (ameaca, seguranca, result) VALUES ('{}', '{}', {});
                                """.format(ameaca, seguranca, result)
                ret = banco.model_create_update(query, "")
                if ret == 0:
                    sg.Popup("Erro ao salvar!")
                else:
                    sg.Popup("Salvo com sucesso!")
                window_inserir.close()
            else:
                window_confirmar.close()
                return
            window_confirmar.close()
        else:
            window_inserir.close()
            return
        window_inserir.close()
    elif funcao == "DRE":
        layout_inserir = [[sg.Text("DRE_D"), sg.Input("", key='dre_d')],
                          [sg.Text("DRE_E"), sg.Input("", key='dre_e')],
                          [sg.Button("Confirmar", key='confirmar'), sg.Button("Cancelar")]]
        window_inserir = sg.Window('Inserir SMI', layout_inserir,
                                   font='Arial 18',
                                   element_justification='center',
                                   auto_size_buttons=True,
                                   auto_size_text=True)
        event, values = window_inserir.read()
        if event == 'confirmar':
            window_inserir.close()
            dre_d = int(values['dre_d'])
            dre_e = int(values['dre_e'])
            result = dre_e / (dre_e + dre_d)
            layout_confirmar = [[sg.Text("RESULTADO SMI")],
                                [sg.Text(str(result))],
                                [sg.Text("Gostaria de salvar o resultado?")],
                                [sg.Button("Confirmar", key='confirmar'), sg.Button("Cancelar", key='cancelar')]]
            window_confirmar = sg.Window('Confirmar inserção', layout_confirmar,
                                         font='Arial 18',
                                         element_justification='center',
                                         auto_size_buttons=True,
                                         auto_size_text=True)
            event, values = window_confirmar.read()
            if event == 'confirmar':
                print("Salvando")
                print("dre_d: {} | dre_e: {}".format(str(dre_d), str(dre_e)))
                print("Result: {}".format(result))
                query = """INSERT INTO DRE (dre_d, dre_e, result) VALUES ({}, {}, {});
                                                """.format(dre_d, dre_e, result)
                ret = banco.model_create_update(query, "")
                if ret == 0:
                    sg.Popup("Erro ao salvar!")
                else:
                    sg.Popup("Salvo com sucesso!")
                window_inserir.close()
            else:
                window_confirmar.close()
                return
            window_confirmar.close()
        else:
            window_inserir.close()
            return
        window_inserir.close()
    elif funcao == "exposicao":
        layout_inserir = [[sg.Text("Exposicao_P"), sg.Input("", key='expo_p')],
                          [sg.Text("Exposicao_C"), sg.Input("", key='expo_c')],
                          [sg.Button("Confirmar", key='confirmar'), sg.Button("Cancelar")]]
        window_inserir = sg.Window('Inserir SMI', layout_inserir,
                                   font='Arial 18',
                                   element_justification='center',
                                   auto_size_buttons=True,
                                   auto_size_text=True)
        event, values = window_inserir.read()
        if event == 'confirmar':
            window_inserir.close()
            expo_p = float(values['expo_p'])
            expo_c = float(values['expo_c'])
            result = expo_p * expo_c
            layout_confirmar = [[sg.Text("RESULTADO EXPOSIÇÃO")],
                                [sg.Text(str(result))],
                                [sg.Text("Gostaria de salvar o resultado?")],
                                [sg.Button("Confirmar", key='confirmar'), sg.Button("Cancelar", key='cancelar')]]
            window_confirmar = sg.Window('Confirmar inserção', layout_confirmar,
                                         font='Arial 18',
                                         element_justification='center',
                                         auto_size_buttons=True,
                                         auto_size_text=True)
            event, values = window_confirmar.read()
            if event == 'confirmar':
                #print("Salvando")
                #print("dre_d: {} | dre_e: {}".format(str(dre_d), str(dre_e)))
                #print("Result: {}".format(result))
                query = """INSERT INTO Exposicao (expo_p, expo_c, result) VALUES ({}, {}, {});
                                                    """.format(expo_p, expo_c, result)
                ret = banco.model_create_update(query, "")
                if ret == 0:
                    sg.Popup("Erro ao salvar!")
                else:
                    sg.Popup("Salvo com sucesso!")
                window_inserir.close()
            else:
                window_confirmar.close()
                return
            window_confirmar.close()
        else:
            window_inserir.close()
            return
        window_inserir.close()
    else:
        return

def atualizar(banco, funcao):
    if funcao == "capacidade":
        query = "SELECT id FROM Capacidade;"
        ids = banco.model_consult(query, "")
        if len(ids) == 0:
            sg.Popup("Erro! Não há dados para serem lidos...")
            return
        layout_selecionar = [[sg.Text("Selecione o ID a ser alterado")],
                             [sg.Combo(ids, key="ids", default_value=ids[0])],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
        window_selecionar = sg.Window('Selecionar ID', layout_selecionar,
                                         font='Arial 18',
                                         element_justification='center',
                                         auto_size_buttons=True,
                                         auto_size_text=True)
        event, values = window_selecionar.read()
        if event == "confirmar":
            window_selecionar.close()
            id = values['ids'][0]
            query = "SELECT * FROM Capacidade WHERE id = {}".format(id)
            editavel = banco.model_consult(query, "")
            print(editavel)
            niveis = ["1 - Processo possue resultados definidos",
                      "2 - A execução é planejada e monitorada",
                      "3 - Pessoas estão preparadas para realizar suas responsabilidades"]
            layout_editar = [[sg.Text("ID"), sg.Input(str(id), disabled=True)],
                             [sg.Text("Nivel"), sg.Combo(niveis, default_value=niveis[editavel[0][1]-1], key="nivel")],
                             [sg.Text("Descrição"), sg.Input(editavel[0][2], key="descricao")],
                             [sg.Text("Fonte"), sg.Input(editavel[0][3], key="fonte")],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
            window_editar = sg.Window('Editar Capacidade', layout_editar,
                                         font='Arial 18',
                                         element_justification='center',
                                         auto_size_buttons=True,
                                         auto_size_text=True)
            event, values = window_editar.read()
            if event == "confirmar":
                query = """
                        UPDATE Capacidade SET
                        nivel = {},
                        descricao = '{}',
                        fonte = {}
                        WHERE id = {};
                        """.format(str(niveis.index(values['nivel'])+1), values['descricao'], str(values['fonte']), str(id))
                ret = banco.model_create_update(query, "")
                if ret == 1:
                    sg.Popup("Editado com sucesso!")
                else:
                    sg.Popup("Falha ao editar!")
                window_editar.close()
            else:
                window_editar.close()
                return
            window_editar.close()
        else:
            window_selecionar.close()
            return
        window_selecionar.close()
    elif funcao == "volume":
        query = "SELECT id FROM Volume;"
        ids = banco.model_consult(query, "")
        if len(ids) == 0:
            sg.Popup("Erro! Não há dados para serem lidos...")
            return
        layout_selecionar = [[sg.Text("Selecione o ID a ser alterado")],
                             [sg.Combo(ids, key="ids", default_value=ids[0])],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
        window_selecionar = sg.Window('Selecionar ID', layout_selecionar,
                                         font='Arial 18',
                                         element_justification='center',
                                         auto_size_buttons=True,
                                         auto_size_text=True)
        event, values = window_selecionar.read()
        if event == "confirmar":
            window_selecionar.close()
            id = values['ids'][0]
            query = "SELECT * FROM Volume WHERE id = {}".format(id)
            editavel = banco.model_consult(query, "")
            print(editavel)
            layout_editar = [[sg.Text("ID"), sg.Input(str(id), disabled=True)],
                             [sg.Text("n1"), sg.Input(editavel[0][1], key="n1")],
                             [sg.Text("n2"), sg.Input(editavel[0][2], key="n2")],
                             [sg.Text("N2"), sg.Input(editavel[0][3], key="N2")],
                             [sg.Text("Resultado"), sg.Input(editavel[0][4], key="Resultado", disabled=True)],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
            window_editar = sg.Window('Editar Capacidade', layout_editar,
                                         font='Arial 18',
                                         element_justification='center',
                                         auto_size_buttons=True,
                                         auto_size_text=True)
            event, values = window_editar.read()
            if event == "confirmar":
                window_editar.close()
                result = (2 / int(values['n1'])) * (int(values['n2']) / int(values['N2']))
                query = """
                        UPDATE Volume SET
                        enep_1 = {},
                        enep_2 = {},
                        eneg_2 = {},
                        result = {}
                        WHERE id = {};
                        """.format(values['n1'], values['n2'], values['N2'], str(result), str(id))
                ret = banco.model_create_update(query, "")
                if ret == 1:
                    sg.Popup("Editado com sucesso!")
                else:
                    sg.Popup("Falha ao editar!")
                window_editar.close()
            else:
                window_editar.close()
                return
            window_editar.close()
        else:
            window_selecionar.close()
            return
        window_selecionar.close()
    elif funcao == "SMI":
        query = "SELECT id FROM SMI;"
        ids = banco.model_consult(query, "")
        if len(ids) == 0:
            sg.Popup("Erro! Não há dados para serem lidos...")
            return
        layout_selecionar = [[sg.Text("Selecione o ID a ser alterado")],
                             [sg.Combo(ids, key="ids", default_value=ids[0])],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
        window_selecionar = sg.Window('Selecionar ID', layout_selecionar,
                                      font='Arial 18',
                                      element_justification='center',
                                      auto_size_buttons=True,
                                      auto_size_text=True)
        event, values = window_selecionar.read()
        if event == "confirmar":
            window_selecionar.close()
            id = values['ids'][0]
            query = "SELECT * FROM SMI WHERE id = {}".format(id)
            editavel = banco.model_consult(query, "")
            print(editavel)
            layout_editar = [[sg.Text("ID"), sg.Input(str(id), disabled=True)],
                             [sg.Text("Mt"), sg.Input(editavel[0][1], key="Mt")],
                             [sg.Text("Fa"), sg.Input(editavel[0][2], key="Fa")],
                             [sg.Text("Fc"), sg.Input(editavel[0][3], key="Fc")],
                             [sg.Text("Fd"), sg.Input(editavel[0][4], key="Fd")],
                             [sg.Text("Resultado"), sg.Input(editavel[0][5], key="Resultado", disabled=True)],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
            window_editar = sg.Window('Editar Capacidade', layout_editar,
                                      font='Arial 18',
                                      element_justification='center',
                                      auto_size_buttons=True,
                                      auto_size_text=True)
            event, values = window_editar.read()
            if event == "confirmar":
                window_editar.close()
                result = (int(values['Mt']) - (int(values['Fa']) + int(values['Fc']) + int(values['Fd']))) / int(values['Mt'])
                print(result)
                query = """
                                UPDATE SMI SET
                                Mt = {},
                                Fa = {},
                                Fc = {},
                                Fd = {},
                                result = {}
                                WHERE id = {};
                                """.format(values['Mt'], values['Fa'], values['Fc'], values['Fd'], str(result), str(id))
                ret = banco.model_create_update(query, "")
                if ret == 1:
                    sg.Popup("Editado com sucesso!")
                else:
                    sg.Popup("Falha ao editar!")
                window_editar.close()
            else:
                window_editar.close()
                return
            window_editar.close()
        else:
            window_selecionar.close()
            return
        window_selecionar.close()
    elif funcao == "integridade":
        query = "SELECT id FROM Integridade;"
        ids = banco.model_consult(query, "")
        if len(ids) == 0:
            sg.Popup("Erro! Não há dados para serem lidos...")
            return
        layout_selecionar = [[sg.Text("Selecione o ID a ser alterado")],
                             [sg.Combo(ids, key="ids", default_value=ids[0])],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
        window_selecionar = sg.Window('Selecionar ID', layout_selecionar,
                                      font='Arial 18',
                                      element_justification='center',
                                      auto_size_buttons=True,
                                      auto_size_text=True)
        event, values = window_selecionar.read()
        if event == "confirmar":
            window_selecionar.close()
            id = values['ids'][0]
            query = "SELECT * FROM Integridade WHERE id = {}".format(id)
            editavel = banco.model_consult(query, "")
            print(editavel)
            layout_editar = [[sg.Text("ID"), sg.Input(str(id), disabled=True)],
                             [sg.Text("Ameaca"), sg.Input(editavel[0][1], key="ameaca")],
                             [sg.Text("Seguranca"), sg.Input(editavel[0][2], key="seguranca")],
                             [sg.Text("Resultado"), sg.Input(editavel[0][3], key="Resultado", disabled=True)],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
            window_editar = sg.Window('Editar Capacidade', layout_editar,
                                      font='Arial 18',
                                      element_justification='center',
                                      auto_size_buttons=True,
                                      auto_size_text=True)
            event, values = window_editar.read()
            if event == "confirmar":
                window_editar.close()
                ameaca = values['ameaca'].split(",")
                seguranca = values['seguranca'].split(",")
                if len(ameaca) != len(seguranca):
                    sg.Popup("Dados para inserção inválidos! Ameaça e Segurança devem ter tamanhos iguais")
                    return
                result = 0
                for i in range(len(seguranca)):
                    result = result + (1 - (float(ameaca[i]) * (1 - float(seguranca[i]))))
                print(result)
                query = """
                                UPDATE Integridade SET
                                ameaca = '{}',
                                seguranca = '{}',
                                result = {}
                                WHERE id = {};
                                """.format(values['ameaca'], values['seguranca'], str(result), str(id))
                ret = banco.model_create_update(query, "")
                if ret == 1:
                    sg.Popup("Editado com sucesso!")
                else:
                    sg.Popup("Falha ao editar!")
                window_editar.close()
            else:
                window_editar.close()
                return
            window_editar.close()
        else:
            window_selecionar.close()
            return
        window_selecionar.close()
    elif funcao == "DRE":
        query = "SELECT id FROM DRE;"
        ids = banco.model_consult(query, "")
        if len(ids) == 0:
            sg.Popup("Erro! Não há dados para serem lidos...")
            return
        layout_selecionar = [[sg.Text("Selecione o ID a ser alterado")],
                             [sg.Combo(ids, key="ids", default_value=ids[0])],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
        window_selecionar = sg.Window('Selecionar ID', layout_selecionar,
                                      font='Arial 18',
                                      element_justification='center',
                                      auto_size_buttons=True,
                                      auto_size_text=True)
        event, values = window_selecionar.read()
        if event == "confirmar":
            window_selecionar.close()
            id = values['ids'][0]
            query = "SELECT * FROM DRE WHERE id = {}".format(id)
            editavel = banco.model_consult(query, "")
            print(editavel)
            layout_editar = [[sg.Text("ID"), sg.Input(str(id), disabled=True)],
                             [sg.Text("DRE_D"), sg.Input(editavel[0][1], key="dre_d")],
                             [sg.Text("DRE_E"), sg.Input(editavel[0][2], key="dre_e")],
                             [sg.Text("Resultado"), sg.Input(editavel[0][3], key="Resultado", disabled=True)],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
            window_editar = sg.Window('Editar Capacidade', layout_editar,
                                      font='Arial 18',
                                      element_justification='center',
                                      auto_size_buttons=True,
                                      auto_size_text=True)
            event, values = window_editar.read()
            if event == "confirmar":
                window_editar.close()
                result = int(values['dre_e']) / (int(values['dre_e']) + int(values['dre_d']))
                print(result)
                query = """
                                UPDATE DRE SET
                                dre_d = {},
                                dre_e = {},
                                result = {}
                                WHERE id = {};
                                """.format(values['dre_e'], values['dre_d'], str(result), str(id))
                ret = banco.model_create_update(query, "")
                if ret == 1:
                    sg.Popup("Editado com sucesso!")
                else:
                    sg.Popup("Falha ao editar!")
                window_editar.close()
            else:
                window_editar.close()
                return
            window_editar.close()
        else:
            window_selecionar.close()
            return
        window_selecionar.close()
    elif funcao == 'exposicao':
        query = "SELECT id FROM Exposicao;"
        ids = banco.model_consult(query, "")
        if len(ids) == 0:
            sg.Popup("Erro! Não há dados para serem lidos...")
            return
        layout_selecionar = [[sg.Text("Selecione o ID a ser alterado")],
                             [sg.Combo(ids, key="ids", default_value=ids[0])],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
        window_selecionar = sg.Window('Selecionar ID', layout_selecionar,
                                      font='Arial 18',
                                      element_justification='center',
                                      auto_size_buttons=True,
                                      auto_size_text=True)
        event, values = window_selecionar.read()
        if event == "confirmar":
            window_selecionar.close()
            id = values['ids'][0]
            query = "SELECT * FROM Exposicao WHERE id = {}".format(id)
            editavel = banco.model_consult(query, "")
            print(editavel)
            layout_editar = [[sg.Text("ID"), sg.Input(str(id), disabled=True)],
                             [sg.Text("expo_p"), sg.Input(editavel[0][1], key="expo_p")],
                             [sg.Text("expo_c"), sg.Input(editavel[0][2], key="expo_c")],
                             [sg.Text("Resultado"), sg.Input(editavel[0][3], key="Resultado", disabled=True)],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
            window_editar = sg.Window('Editar Capacidade', layout_editar,
                                      font='Arial 18',
                                      element_justification='center',
                                      auto_size_buttons=True,
                                      auto_size_text=True)
            event, values = window_editar.read()
            if event == "confirmar":
                result = int(values['expo_p']) * int(values['expo_c'])
                print(result)
                query = """
                                UPDATE Exposicao SET
                                expo_p = {},
                                expo_c = {},
                                result = {}
                                WHERE id = {};
                                """.format(values['expo_p'], values['expo_c'], str(result), str(id))
                ret = banco.model_create_update(query, "")
                if ret == 1:
                    sg.Popup("Editado com sucesso!")
                else:
                    sg.Popup("Falha ao editar!")
                window_editar.close()
            else:
                window_editar.close()
                return
            window_editar.close()
        else:
            window_selecionar.close()
            return
        window_selecionar.close()
    else:
        return

def deletar(banco, funcao):
    if funcao == "capacidade":
        query = "SELECT id FROM Capacidade;"
        ids = banco.model_consult(query, "")
        if len(ids) == 0:
            sg.Popup("Erro! Não há dados para serem lidos...")
            return
        layout_selecionar = [[sg.Text("Selecione o ID a ser alterado")],
                             [sg.Combo(ids, key="ids", default_value=ids[0])],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
        window_selecionar = sg.Window('Selecionar ID', layout_selecionar,
                                      font='Arial 18',
                                      element_justification='center',
                                      auto_size_buttons=True,
                                      auto_size_text=True)
        event, values = window_selecionar.read()
        if event == "confirmar":
            window_selecionar.close()
            query = "DELETE FROM Capacidade WHERE id = {}".format(values['ids'][0])
            ret = banco.model_create_update(query, "")
            if ret == 1:
                sg.Popup("Salvo com sucesso!")
            else:
                sg.Popup("Erro ao salvar!")
        else:
            window_selecionar.close()
        window_selecionar.close()
    elif funcao == "volume":
        query = "SELECT id FROM Volume;"
        ids = banco.model_consult(query, "")
        if len(ids) == 0:
            sg.Popup("Erro! Não há dados para serem lidos...")
            return
        layout_selecionar = [[sg.Text("Selecione o ID a ser alterado")],
                             [sg.Combo(ids, key="ids", default_value=ids[0])],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
        window_selecionar = sg.Window('Selecionar ID', layout_selecionar,
                                      font='Arial 18',
                                      element_justification='center',
                                      auto_size_buttons=True,
                                      auto_size_text=True)
        event, values = window_selecionar.read()
        if event == "confirmar":
            window_selecionar.close()
            query = "DELETE FROM Volume WHERE id = {}".format(values['ids'][0])
            ret = banco.model_create_update(query, "")
            if ret == 1:
                sg.Popup("Salvo com sucesso!")
            else:
                sg.Popup("Erro ao salvar!")
        else:
            window_selecionar.close()
        window_selecionar.close()
    elif funcao == "SMI":
        query = "SELECT id FROM SMI;"
        ids = banco.model_consult(query, "")
        if len(ids) == 0:
            sg.Popup("Erro! Não há dados para serem lidos...")
            return
        layout_selecionar = [[sg.Text("Selecione o ID a ser alterado")],
                             [sg.Combo(ids, key="ids", default_value=ids[0])],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
        window_selecionar = sg.Window('Selecionar ID', layout_selecionar,
                                      font='Arial 18',
                                      element_justification='center',
                                      auto_size_buttons=True,
                                      auto_size_text=True)
        event, values = window_selecionar.read()
        if event == "confirmar":
            window_selecionar.close()
            query = "DELETE FROM SMI WHERE id = {}".format(values['ids'][0])
            ret = banco.model_create_update(query, "")
            if ret == 1:
                sg.Popup("Salvo com sucesso!")
            else:
                sg.Popup("Erro ao salvar!")
        else:
            window_selecionar.close()
        window_selecionar.close()
    elif funcao == "integridade":
        query = "SELECT id FROM Integridade;"
        ids = banco.model_consult(query, "")
        if len(ids) == 0:
            sg.Popup("Erro! Não há dados para serem lidos...")
            return
        layout_selecionar = [[sg.Text("Selecione o ID a ser alterado")],
                             [sg.Combo(ids, key="ids", default_value=ids[0])],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
        window_selecionar = sg.Window('Selecionar ID', layout_selecionar,
                                      font='Arial 18',
                                      element_justification='center',
                                      auto_size_buttons=True,
                                      auto_size_text=True)
        event, values = window_selecionar.read()
        if event == "confirmar":
            window_selecionar.close()
            query = "DELETE FROM Integridade WHERE id = {}".format(values['ids'][0])
            ret = banco.model_create_update(query, "")
            if ret == 1:
                sg.Popup("Salvo com sucesso!")
            else:
                sg.Popup("Erro ao salvar!")
        else:
            window_selecionar.close()
        window_selecionar.close()
    elif funcao == "DRE":
        query = "SELECT id FROM DRE;"
        ids = banco.model_consult(query, "")
        if len(ids) == 0:
            sg.Popup("Erro! Não há dados para serem lidos...")
            return
        layout_selecionar = [[sg.Text("Selecione o ID a ser alterado")],
                             [sg.Combo(ids, key="ids", default_value=ids[0])],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
        window_selecionar = sg.Window('Selecionar ID', layout_selecionar,
                                      font='Arial 18',
                                      element_justification='center',
                                      auto_size_buttons=True,
                                      auto_size_text=True)
        event, values = window_selecionar.read()
        if event == "confirmar":
            window_selecionar.close()
            query = "DELETE FROM DRE WHERE id = {}".format(values['ids'][0])
            ret = banco.model_create_update(query, "")
            if ret == 1:
                sg.Popup("Salvo com sucesso!")
            else:
                sg.Popup("Erro ao salvar!")
        else:
            window_selecionar.close()
        window_selecionar.close()
    elif funcao == 'exposicao':
        query = "SELECT id FROM Exposicao;"
        ids = banco.model_consult(query, "")
        if len(ids) == 0:
            sg.Popup("Erro! Não há dados para serem lidos...")
            return
        layout_selecionar = [[sg.Text("Selecione o ID a ser alterado")],
                             [sg.Combo(ids, key="ids", default_value=ids[0])],
                             [sg.Button("Confirmar", key="confirmar"), sg.Button("Cancelar", key="cancelar")]]
        window_selecionar = sg.Window('Selecionar ID', layout_selecionar,
                                      font='Arial 18',
                                      element_justification='center',
                                      auto_size_buttons=True,
                                      auto_size_text=True)
        event, values = window_selecionar.read()
        if event == "confirmar":
            window_selecionar.close()
            query = "DELETE FROM Exposicao WHERE id = {}".format(values['ids'][0])
            print(query)
            ret = banco.model_create_update(query, "")
            if ret == 1:
                sg.Popup("Salvo com sucesso!")
            else:
                sg.Popup("Erro ao salvar!")
        else:
            window_selecionar.close()
        window_selecionar.close()
    else:
        return

def consultar(banco, funcao):
    if funcao == "capacidade":
        query = "SELECT * FROM Capacidade ORDER BY nivel;"
        rets = banco.model_consult(query, "")
        if len(rets) == 0:
            sg.Popup("Não há dados para consultar!")
            return
        out = ""
        out = out + "-- NIVEL 1 --\n"
        out = out + "   ID | DESCRICAO | FONTE\n"
        for i in range(len(rets)):
            if rets[i][1] != 1:
                continue
            out = out + "   "
            out = out + "{} | {} | {}\n".format(rets[i][0], rets[i][2], rets[i][3])
        out = out + "-- NIVEL 2 --\n"
        out = out + "   ID | DESCRICAO | FONTE\n"
        for i in range(len(rets)):
            if rets[i][1] != 2:
                continue
            out = out + "   "
            out = out + "{} | {} | {}\n".format(rets[i][0], rets[i][2], rets[i][3])
        out = out + "-- NIVEL 3 --\n"
        out = out + "   ID | DESCRICAO | FONTE\n"
        for i in range(len(rets)):
            if rets[i][1] != 3:
                continue
            out = out + "   "
            out = out + "{} | {} | {}\n".format(rets[i][0], rets[i][2], rets[i][3])
        out = out + "--------------------"
        try:
            f = open("out.txt", 'w')
            f.write(out)
            f.close()
        except OSError as e:
            print(e)
        os.startfile("out.txt")
    elif funcao == "volume":
        query = "SELECT * FROM Volume"
        rets = banco.model_consult(query, "")
        if len(rets) == 0:
            sg.Popup("Não há dados para consultar!")
            return
        out = "ID | n1 | n2 | N2 | RESULTADO\n"
        for i in range(len(rets)):
            out = out + "{} | {} | {} | {} | {}\n".format(rets[i][0], rets[i][1], rets[i][2], rets[i][3], rets[i][4])
        out = out + "--------------------"
        try:
            f = open("out.txt", 'w')
            f.write(out)
            f.close()
        except OSError as e:
            print(e)
        os.startfile("out.txt")
    elif funcao == "SMI":
        query = "SELECT * FROM SMI;"
        rets = banco.model_consult(query, "")
        if len(rets) == 0:
            sg.Popup("Não há dados para consultar!")
            return
        out = "ID | Mt | Fc | Fa | Fd | RESULTADO\n"
        for i in range(len(rets)):
            out = out + "{} | {} | {} | {} | {} | {} \n".format(rets[i][0], rets[i][1], rets[i][2], rets[i][3], rets[i][4], rets[i][5])
        out = out + "--------------------"
        try:
            f = open("out.txt", 'w')
            f.write(out)
            f.close()
        except OSError as e:
            print(e)
        os.startfile("out.txt")
    elif funcao == "integridade":
        query = "SELECT * FROM Integridade;"
        rets = banco.model_consult(query, "")
        print(rets)
        if len(rets) == 0:
            sg.Popup("Não há dados para consultar!")
            return
        out = ""
        for i in range(len(rets)):
            out = out + "PROBLEMA {}\n".format(rets[i][0])
            ameaca = rets[i][1].split(',')
            seguranca = rets[i][2].split(',')
            out = out +  "AMEACA | SEGURANCA | INTEGRIDADE\n"
            for e in ameaca:
                out = out + e + " "
            out = out + "| "
            for e in seguranca:
                out = out + e + " "
            out = out + "| "
            out = out + "{} \n".format(rets[0][3])
        out = out + "--------------------"
        try:
            f = open("out.txt", 'w')
            f.write(out)
            f.close()
        except OSError as e:
            print(e)
        os.startfile("out.txt")
    elif funcao == "DRE":
        query = "SELECT * FROM DRE;"
        rets = banco.model_consult(query, "")
        if len(rets) == 0:
            sg.Popup("Não há dados para consultar!")
            return
        out = "ID | DRE_D | DRE_E | RESULTADO\n"
        for i in range(len(rets)):
            out = out + "{} | {} | {} | {} \n".format(rets[i][0], rets[i][1], rets[i][2], rets[i][3])
        out = out + "--------------------"
        try:
            f = open("out.txt", 'w')
            f.write(out)
            f.close()
        except OSError as e:
            print(e)
        os.startfile("out.txt")
    elif funcao == "exposicao":
        query = "SELECT * FROM Exposicao;"
        rets = banco.model_consult(query, "")
        if len(rets) == 0:
            sg.Popup("Não há dados para consultar!")
            return
        out = "ID | Expo_P | Expo_C | RESULTADO\n"
        for i in range(len(rets)):
            out = out + "{} | {} | {} | {} \n".format(rets[i][0], rets[i][1], rets[i][2], rets[i][3])
        out = out + "--------------------"
        try:
            f = open("out.txt", 'w')
            f.write(out)
            f.close()
        except OSError as e:
            print(e)
        os.startfile("out.txt")
    else:
        return

main()
