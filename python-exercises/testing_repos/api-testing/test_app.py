import json
import pytest
import server


def test_api_get_dogs(api):
    res = api.get('/api/dogs')
    assert res.json == {'dogs': [{'id': 1, 'name': 'Mochi'}, {'id': 2, 'name': 'Masha'}]}

def test_api_get_dog(api):
    res = api.get('/api/dogs/2')
    assert res.json['dog']['name'] == 'Masha'

def test_api_post_dogs(api):
    mock_data = json.dumps({'name': 'Molly'})
    mock_headers = {'Content-Type': 'application/json'}
    res = api.post('/api/dogs', data=mock_data, headers=mock_headers)
    assert res.json['dog']['id'] == 3

def test_api_not_found(api):
    res = api.get('/bob')
    assert res.status == '404 NOT FOUND'
    assert 'Oops!' in res.json['message']
    
# def test_api_debug(api):
#     assert api.application.debug == False
    
# def test_run_app():
#     with pytest.raises(SystemExit) as sys_exit:
#         server.app.run(debug=True)
#     assert sys_exit.type == SystemExit
#     assert sys_exit.value.code == 0

 
    
# import subprocess
# import time

# def test_app_run_output():
#     # Start the server in a separate process
#     process = subprocess.Popen(['python', 'server.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     # Wait for the server to start up (optional)
#     time.sleep(1)

#     # Check the output of the process
#     out, err = process.communicate()
#     print("Process output:", out.decode())
#     print("Process error:", err.decode())

#     # Assert and test the output
#     assert "__main__" in out.decode()
#     assert "Error message" not in err.decode()
