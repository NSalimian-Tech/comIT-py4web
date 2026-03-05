# Last time modified: 03/05/26
# Author: Najme

html_base = ""

with open("garbage.html", "r") as website:
    html_base = website.read()
    

page_title = "MY Python Website"

html_modified = html_base.replace("<title>Document", f"<title>{page_title}") 

# print(html_modified)

daisy_ui ="""

<!-- Daisy UI -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<!-- Daisy ui themes -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />

"""

html_modified = html_modified.replace("</head>", daisy_ui +"\n</head>" )

theme = "dracula"
html_modified = html_modified.replace('<html lang="en">', f'<html lang="en" data-theme="{theme}">')

nav_bar = """
<div class="navbar bg-base-100 shadow-sm">
  <a class="btn btn-ghost text-xl">daisyUI</a>
</div>
"""


html_modified = html_modified.replace('<body>', '<body>\n'+nav_bar)

my_english_hero = """
<div class="hero min-h-screen shadow-2xl bg-base-100 mt-10 rounded-box">
  <div class="hero-content text-center">
    <div class="max-w-md">
      <h1 class="text-5xl font-bold text-accent">Hello there!</h1>
      <p class="py-6">This website was built using Python to automate the HTML editing process. We used Daisy UI components for styling.</p>
      <button class="btn btn-secondary">Get Started</button>
    </div>
  </div>
</div>
"""

# This is a "Pricing" table element
my_english_pricing = """
<div class="flex flex-wrap justify-center gap-4 p-10">
  <div class="card w-80 bg-neutral text-neutral-content shadow-xl">
    <div class="card-body items-center text-center">
      <h2 class="card-title text-warning">Starter</h2>
      <p>Perfect for students</p>
      <div class="text-4xl font-bold">$0 / mo</div>
      <div class="card-actions mt-4">
        <button class="btn btn-outline btn-warning">Sign Up</button>
      </div>
    </div>
  </div>
</div>
"""

# Step 2: Use </body> as reference to replace and add elements on top of it
# We combine our variables and put them before the </body> tag
html_modified = html_modified.replace("</body>", my_english_hero + my_english_pricing + "\n</body>")

# Final Step: Saving everything into index.html
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_modified)

print("Process finished! Check index.html for the new English components.")
# --- MY ASSIGNMENT END ---
