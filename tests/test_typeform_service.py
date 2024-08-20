import unittest
from unittest.mock import patch, MagicMock
from src.typeform.typeform_service import TypeformService

class TestTypeformService(unittest.TestCase):
    def setUp(self):
        self.token = 'test_token'
        self.form_id = 'test_form_id'
        self.typeform_service = TypeformService(self.token, self.form_id)

    @patch('requests.patch')
    def test_update_form_success(self, mock_patch):
        # Mockando a resposta da API
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": "success"}
        mock_patch.return_value = mock_response

        # Dados de teste
        data = {"fields": []}

        # Executando o método
        response = self.typeform_service.update_form(data)

        # Verificando os resultados
        self.assertEqual(response, {"result": "success"})
        mock_patch.assert_called_once_with(
            f'https://api.typeform.com/forms/{self.form_id}',
            json=data,
            headers={'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'}
        )

    @patch('requests.patch')
    def test_update_form_failure(self, mock_patch):
        # Mockando uma falha na API
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.raise_for_status.side_effect = Exception("Bad Request")
        mock_patch.return_value = mock_response

        # Dados de teste
        data = {"fields": []}

        # Verificando que a exceção é levantada
        with self.assertRaises(Exception) as context:
            self.typeform_service.update_form(data)

        self.assertTrue('Bad Request' in str(context.exception))
