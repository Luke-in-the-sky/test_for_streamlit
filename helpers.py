import requests

def download_file_from_google_drive(id: str, destination: str):
  """
  Downloads a publicly-accessible file from Google Drive
  See https://bit.ly/3gliBne

  id: the id fo the file (eg from the sharable link)
  destination: path where to store the downloaded file
  """
  def get_confirm_token(response):
      for key, value in response.cookies.items():
          if key.startswith('download_warning'):
              return value
      return None

  def save_response_content(response, destination):
      CHUNK_SIZE = 32768
      with open(destination, "wb") as f:
          for chunk in response.iter_content(CHUNK_SIZE):
              if chunk: # filter out keep-alive new chunks
                  f.write(chunk)

  URL = "https://docs.google.com/uc?export=download"
  session = requests.Session()
  response = session.get(URL, params = { 'id' : id }, stream = True)
  token = get_confirm_token(response)

  if token:
      params = { 'id' : id, 'confirm' : token }
      response = session.get(URL, params = params, stream = True)
  save_response_content(response, destination)