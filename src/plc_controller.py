"""
plc_controller.py

Lógica principal do CLP (Controlador Lógico Programável) simulado.
Reproduz o ciclo de scan típico de um CLP real (leitura de entradas,
execução da lógica, atualização de saídas), aplicado ao controle de
uma esteira transportadora.
"""

import time
from actuators import ConveyorMotor
from sensors import OpticalSensor, JamSensor, EmergencyStopButton


class PLCController:
    """
    Simula o ciclo de scan de um CLP controlando uma esteira transportadora.

    Fluxo:
    1. Lê sensores de entrada e saída da peça
    2. Lê o sensor de engasgamento (jam)
    3. Lê o botão de emergência
    4. Aciona ou desliga o motor da esteira conforme a lógica
    """

    def __init__(self):
        self.entry_sensor = OpticalSensor("Sensor de Entrada")
        self.exit_sensor = OpticalSensor("Sensor de Saída")
        self.jam_sensor = JamSensor("Sensor de Engasgamento")
        self.emergency_stop = EmergencyStopButton("Botão de Emergência")
        self.motor = ConveyorMotor("Motor da Esteira")
        self.running = False

    def scan_cycle(self):
        """Executa um ciclo de varredura do CLP (scan cycle)."""

        # 1. Leitura das entradas
        emergency_active = self.emergency_stop.read()
        jam_detected = self.jam_sensor.check_jam()
        entry_detected = self.entry_sensor.read()

        # 2. Lógica de controle
        if emergency_active:
            self.motor.stop()
            self.running = False
            print("[ALERTA] Parada de emergência ativada!")
            return

        if jam_detected:
            self.motor.stop()
            self.running = False
            print("[ALERTA] Engasgamento detectado na esteira!")
            return

        if entry_detected and not self.running:
            self.motor.start()
            self.running = True
            print("[INFO] Peça detectada. Esteira em movimento.")

        # 3. Atualização de saídas
        if self.running:
            self.motor.run()

    def simulate(self, cycles: int = 10, interval: float = 1.0):
        """Executa a simulação por um número determinado de ciclos."""
        print("=== Iniciando simulação do CLP ===")
        for i in range(cycles):
            print(f"\n--- Ciclo {i + 1} ---")
            self.scan_cycle()
            time.sleep(interval)
        print("\n=== Simulação encerrada ===")


if __name__ == "__main__":
    plc = PLCController()
    plc.entry_sensor.trigger()  # simula chegada de uma peça
    plc.simulate(cycles=5, interval=0.5)
