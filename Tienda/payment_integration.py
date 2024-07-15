import requests

class PaymentClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def create(self, body):
        url = f"{self.base_url}/api/payment/create"  # Reemplaza con la URL correcta de la API de pagos
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer your_token_here'  # Reemplaza con el token de autorización adecuado
        }
        
        try:
            response = requests.post(url, json=body, headers=headers)
            response.raise_for_status()  # Lanza una excepción para errores HTTP
            return response.json()  # Devuelve la respuesta JSON como diccionario Python
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la solicitud: {e}")
            return None
