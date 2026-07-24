"""
hmi.py

Interface HMI (Human-Machine Interface) simplificada — simula o painel de
supervisório que um operador usaria para acompanhar o estado da esteira
transportadora em tempo real (equivalente a uma tela SCADA/HMI industrial).
"""

from plc_controller import PLCController


class HMIDisplay:
    """
    Simula um painel de supervisório exibindo o estado atual do sistema:
    sensores, motor e alarmes.
    """

    def __init__(self, plc: PLCController):
        self.plc = plc

    def render(self):
        """Exibe o estado atual do sistema, como uma tela HMI faria."""
        print("\n========== PAINEL HMI ==========")
        print(f"Sensor de Entrada   : {'ATIVO' if self.plc.entry_sensor.read() else 'inativo'}")
        print(f"Sensor de Saída     : {'ATIVO' if self.plc.exit_sensor.read() else 'inativo'}")
        print(f"Engasgamento (Jam)  : {'ALARME' if self.plc.jam_sensor.read() else 'normal'}")
        print(f"Emergência          : {'ACIONADA' if self.plc.emergency_stop.read() else 'normal'}")
        print(f"Motor da Esteira    : {'LIGADO' if self.plc.running else 'desligado'}")
        print("=================================")

    def run_with_display(self, cycles: int = 10, interval: float = 1.0):
        """Executa a simulação do CLP exibindo o painel a cada ciclo."""
        import time

        print("=== HMI conectada ao CLP ===")
        for i in range(cycles):
            print(f"\n--- Ciclo {i + 1} ---")
            self.plc.scan_cycle()
            self.render()
            time.sleep(interval)


if __name__ == "__main__":
    plc = PLCController()
    hmi = HMIDisplay(plc)

    plc.entry_sensor.trigger()  # simula chegada de uma peça
    hmi.run_with_display(cycles=5, interval=0.5)
