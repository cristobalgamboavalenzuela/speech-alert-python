import speech_recognition as sr
import pyttsx3
import tkinter as tk
from threading import Thread

# Lista de palabras clave
palabras_clave = [
 "centinela","centella","centinella","cenella","cenela","centenera",
 "radares","radar","ralar","raar",
 "geotecnia",
 ]  

print("iniciando detección de voz")
print("... programa en desarrollo")
# Inicializa el motor de voz
motor = pyttsx3.init()

# Inicializa reconocimiento y micrófono
r = sr.Recognizer()

# es posible hacer que se detecten diferentes sonidos, con esto me refiero a si quieres qeu detecte lo que escucha el micrófono
# o los propios sonidos del sistema como youtube por ejemplo o la radio, sin la necesidad de un micrfono o contaminacion del ambiente
# para eso hay que activar  "stereo mix" o "mezcla estéreo" en los dispositivos de grabación
# al correr la siguiente linea se despliega una lista con todos los dispositivos y hay que elegir ese,
# con la línea de código " mic = sr.Microphone(device_index=1) "
# la otra opción es simplemente elegir el micrófono por defecto, 
# para lo que hay que poner " mic = sr.Microphone() "
#

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{index}: {name}")


#mic = sr.Microphone()
mic = sr.Microphone(device_index=12)

# Función para mostrar el popup
def mostrar_alerta(mensaje):
    def cerrar_ventana():
        ventana.destroy()

    ventana = tk.Tk()
    ventana.title("⚠️ ALERTA DE RADIO ⚠️")
    ventana.geometry("1920x1080")
    ventana.configure(bg="yellow")
    etiqueta = tk.Label(ventana, text=mensaje, font=("Arial", 30, "bold"), bg="yellow", fg="red")
    etiqueta.pack(pady=40)
    ventana.after(5000, cerrar_ventana)  # Cierra automáticamente en 5 segundos
    ventana.mainloop()

# Comienza a escuchar
print("🎙️ Escuchando audio ambiente...")

with mic as source:
    r.adjust_for_ambient_noise(source)

    while True:
        try:
            audio = r.listen(source)
            texto = r.recognize_google(audio, language="es-ES")
            print("Escuchado:", texto)

            for palabra in palabras_clave:
                if palabra.lower() in texto.lower():
                    mensaje = f"Se dijo: {palabra}"
                    print(f"🔔 {mensaje}")
                    # Alerta de voz
                    motor.say(f"Atención, dijeron {palabra}")
                    motor.runAndWait()
                    # Mostrar ventana emergente
                    Thread(target=mostrar_alerta, args=(mensaje,), daemon=True).start()
                    break  # No repetir si hay varias palabras

        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print("Error con el reconocimiento:", e)
