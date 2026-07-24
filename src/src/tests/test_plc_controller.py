"""
test_plc_controller.py

Testes automatizados da lógica do CLP simulado, validando o comportamento
do sistema em cenários normais e de falha (engasgamento, parada de emergência).
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from plc_controller import PLCController


def test_motor_liga_ao_detectar_peca():
    """O motor deve ligar quando o sensor de entrada detecta uma peça."""
    plc = PLCController()
    plc.entry_sensor.trigger()
    plc.scan_cycle()
    assert plc.running is True


def test_motor_para_em_emergencia():
    """O motor deve parar imediatamente se o botão de emergência for acionado."""
    plc = PLCController()
    plc.entry_sensor.trigger()
    plc.scan_cycle()  # liga o motor
    assert plc.running is True

    plc.emergency_stop.press()
    plc.scan_cycle()
    assert plc.running is False


def test_motor_para_em_engasgamento():
    """O motor deve parar se o sensor de engasgamento (jam) for ativado."""
    plc = PLCController()
    plc.entry_sensor.trigger()
    plc.scan_cycle()  # liga o motor
    assert plc.running is True

    plc.jam_sensor.jam_probability = 1.0  # força a ocorrência do jam
    plc.scan_cycle()
    assert plc.running is False


def test_estado_inicial_motor_desligado():
    """Ao iniciar, o motor deve estar desligado por padrão."""
    plc = PLCController()
    assert plc.running is False


if __name__ == "__main__":
    test_motor_liga_ao_detectar_peca()
    test_motor_para_em_emergencia()
    test_motor_para_em_engasgamento()
    test_estado_inicial_motor_desligado()
    print("Todos os testes passaram com sucesso!")
