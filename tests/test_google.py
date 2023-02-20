import requests


class TestGoogleSearch():

    def test_page_access(self, init_test):

        response = requests.get(init_test)

        assert response.status_code == 200, 'status code not correct'
        
    def test_page_404(self):
        response = requests.get('https://www.google.com/qwe')
        
        assert response.status_code == 200, 'status code not correct'
