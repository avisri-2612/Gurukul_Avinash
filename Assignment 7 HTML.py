# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>My Themed Webpage</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             margin: 0;
#             padding: 0;
#             background-color: #f4f4f9;
#         }
#         header {
#             background-color: #4CAF50;
#             color: white;
#             padding: 20px;
#             text-align: center;
#         }
#         .container {
#             padding: 20px;
#             max-width: 800px;
#             margin: auto;
#         }
#         form {
#             margin-top: 20px;
#         }
#         form input, form select, form textarea {
#             display: block;
#             width: 100%;
#             padding: 10px;
#             margin: 10px 0;
#             border: 1px solid #ddd;
#             border-radius: 5px;
#         }
#         form button {
#             background-color: #4CAF50;
#             color: white;
#             padding: 10px;
#             border: none;
#             border-radius: 5px;
#             cursor: pointer;
#         }
#         form button:hover {
#             background-color: #45a049;
#         }
#         .media {
#             text-align: center;
#             margin-top: 20px;
#         }
#         .media img {
#             max-width: 100%;
#             height: auto;
#             border-radius: 10px;
#         }
#     </style>
# </head>
# <body>
#     <header>
#         <h1>Welcome to My Themed Webpage</h1>
#     </header>
#     <div class="container">
#         <h2>Page Title: User Information Portal</h2>
#         <form>
#             <label for="name">Full Name:</label>
#             <input type="text" id="name" name="name" placeholder="Enter your full name" required>
#
#             <label for="email">Email:</label>
#             <input type="email" id="email" name="email" placeholder="Enter your email" required>
#
#             <label for="gender">Gender:</label>
#             <select id="gender" name="gender">
#                 <option value="male">Male</option>
#                 <option value="female">Female</option>
#                 <option value="other">Other</option>
#             </select>
#
#             <label for="message">Message:</label>
#             <textarea id="message" name="message" rows="4" placeholder="Enter your message here..."></textarea>
#
#             <button type="submit">Submit</button>
#         </form>
#
#         <div class="media">
#             <h3>Theme Image:</h3>
#             <img src="https://images.pexels.com/photos/443383/pexels-photo-443383.jpeg" alt="Themed High-Rise Buildings">
#         </div>
#     </div>
# </body>
# </html>