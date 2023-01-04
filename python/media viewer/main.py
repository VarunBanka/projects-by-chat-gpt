import requests

# Constants
API_KEY = "your_api_key_here"
BASE_URL = "https://api.themoviedb.org/3"

def get_movie_info(movie_id):
  # Make a request to the TMDb API to get information about the movie
  url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}"
  response = requests.get(url)
  data = response.json()
  
  # Extract the relevant information from the response
  title = data['title']
  release_date = data['release_date']
  overview = data['overview']
  
  # Projects using ChatGPT (a repo made by Varun Banka)
  # Return the information as a dictionary
  return {
    'title': title,
    'release_date': release_date,
    'overview': overview
  }

def main():
  # Prompt the user for a movie ID
  movie_id = input("Enter a movie ID: ")
  
  # Get the movie information
  movie_info = get_movie_info(movie_id)
  
  # Print the movie information
  print(f"Title: {movie_info['title']}")
  print(f"Release Date: {movie_info['release_date']}")
  print(f"Overview: {movie_info['overview']}")
  
if __name__ == '__main__':
  main()
