import webbrowser
import pyperclip

class Browser:
  def __init__(self):
    self.history = []
  
  def visit_website(self, url):
    webbrowser.open(url)
    self.history.append(url)
  
  def go_back(self):
    if self.history:
      last_visited = self.history.pop()
      self.visit_website(last_visited)
    else:
      print("You have no browsing history.")
  
  def search(self, query):
    self.visit_website(f"https://www.google.com/search?q={query}")
  
  def copy_url(self):
    url = pyperclip.paste()
    if url:
      self.history.append(url)
      print("URL copied to clipboard and added to history.")
    else:
      print("No URL found in clipboard.")

# Example usage
browser = Browser()

browser.search("python programming")

browser.copy_url()

browser.go_back()
