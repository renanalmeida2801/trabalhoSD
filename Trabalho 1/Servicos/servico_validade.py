from Interface.perecivel import Perecivel

class ServicoValidade:
    def __init__(self, produtos):
        self.produtos = produtos

    def checar_vencidos(self, data_atual:str):
        for p in self.produtos:
            if isinstance(p, Perecivel):
                if(p.esta_vencido(data_atual)):
                    print(f"[VENCIDO] {p.nome} - Validade {p.validade}")
                else: 
                    print(f"[OK] {p.nome} - validade{p.validade}")