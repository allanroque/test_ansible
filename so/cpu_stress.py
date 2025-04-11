import threading
import time
import math

def stress_cpu():
    while True:
        # Loop matemático pesado
        for _ in range(1000000):
            math.sqrt(12345.6789)

def main():
    num_threads = 4  # Aumente conforme quiser gerar mais carga
    print(f"🔁 Gerando carga com {num_threads} threads. Pressione Ctrl+C para parar.")
    threads = []

    for _ in range(num_threads):
        t = threading.Thread(target=stress_cpu)
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Carga interrompida.")

if __name__ == "__main__":
    main()
