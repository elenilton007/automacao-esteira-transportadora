"""
actuators.py

Simulação dos atuadores do sistema de automação da esteira transportadora.
Em um CLP real, esses componentes seriam acionados por saídas digitais (DO),
controlando relés, contatores ou variadores de frequência conectados a motores.
"""


class ConveyorMotor:
    """
    Simula o motor da esteira transportadora, acionado por uma saída
    digital do CLP (equivalente a um contator ou variador de frequência).
    """

    def __init__(self, name: str):
        self.name = name
        self.is_running = False

    def start(self):
        """Liga o motor da esteira."""
        self.is_running = True

    def stop(self):
        """Desliga o motor da esteira."""
        self.is_running = False

    def run(self):
        """Mantém o motor em funcionamento durante o ciclo de scan."""
        if self.is_running:
            pass  # aqui entraria a lógica de acionamento físico real

    def __repr__(self):
        return f"<ConveyorMotor {self.name}: {'LIGADO' if self.is_running else 'desligado'}>"
