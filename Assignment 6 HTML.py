# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Job Application</title>
#     <style>
#         /* Page styling */
#         body {
#             font-family: Arial, sans-serif;
#             color: #333;
#             margin: 0;
#             padding: 0;
#             background: url('https://via.placeholder.com/1500x1000/87CEFA/000000?text=Background+Image') no-repeat center fixed;
#             background-size: cover;
#         }
#
#         /* Adding a blue overlay on top of the background */
#         .overlay {
#             position: absolute;
#             top: 0;
#             left: 0;
#             width: 100%;
#             height: 100%;
#             background-color: rgba(0, 0, 139, 0.5); /* Dark blue with transparency */
#             z-index: 1;
#         }
#
#         /* Centering the content */
#         .container {
#             position: relative;
#             z-index: 2;
#             max-width: 600px;
#             margin: 50px auto;
#             padding: 20px;
#             background-color: rgba(255, 255, 255, 0.9); /* White with slight transparency */
#             box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
#             border-radius: 8px;
#             color: #333;
#         }
#
#         /* Header and form styles */
#         header {
#             background-color: #4CAF50;
#             color: white;
#             padding: 15px;
#             text-align: center;
#             font-size: 24px;
#             font-weight: bold;
#             border-radius: 8px 8px 0 0;
#         }
#
#         h2 {
#             color: #4CAF50;
#             text-align: center;
#         }
#
#         .form-group {
#             margin-bottom: 15px;
#         }
#
#         .form-group label {
#             display: block;
#             font-weight: bold;
#             margin-bottom: 5px;
#         }
#
#         .form-group input, .form-group textarea, .form-group select {
#             width: 100%;
#             padding: 8px;
#             border: 1px solid #ccc;
#             border-radius: 4px;
#         }
#
#         .form-group input[type="submit"] {
#             background-color: #4CAF50;
#             color: white;
#             border: none;
#             cursor: pointer;
#             font-size: 16px;
#         }
#
#         .form-group input[type="submit"]:hover {
#             background-color: #45a049;
#         }
#
#         .form-image {
#             text-align: center;
#             margin: 20px 0;
#         }
#
#         .form-image img {
#             width: 100%;
#             max-width: 200px;
#             border-radius: 8px;
#         }
#     </style>
# </head>
# <body>
#
# <div class="overlay"></div> <!-- Blue overlay background -->
#
# <header>Job Application Portal</header>
#
# <div class="container">
#     <h2>Apply for Your Dream Job</h2>
#     <p>Please fill out the form below with your details to apply for the position.</p>
#
#     <!-- Image related to job applications -->
#     <div class="form-image">
#         <img src="https://via.placeholder.com/200" alt="Job Application Image">
#     </div>
#
#     <!-- Job Application Form -->
#     <form action="#" method="post">
#         <!-- Personal Information -->
#         <div class="form-group">
#             <label for="name">Full Name</label>
#             <input type="text" id="name" name="name" required>
#         </div>
#
#         <div class="form-group">
#             <label for="email">Email Address</label>
#             <input type="email" id="email" name="email" required>
#         </div>
#
#         <div class="form-group">
#             <label for="phone">Phone Number</label>
#             <input type="tel" id="phone" name="phone" required>
#         </div>
#
#         <!-- Work Experience -->
#         <div class="form-group">
#             <label for="experience">Work Experience</label>
#             <textarea id="experience" name="experience" rows="4" placeholder="Describe your work experience" required></textarea>
#         </div>
#
#         <!-- Education -->
#         <div class="form-group">
#             <label for="education">Highest Level of Education</label>
#             <select id="education" name="education">
#                 <option value="high school">High School</option>
#                 <option value="bachelor">Bachelor's Degree</option>
#                 <option value="master">Master's Degree</option>
#                 <option value="phd">PhD</option>
#             </select>
#         </div>
#
#         <!-- Submit Button -->
#         <div class="form-group">
#             <input type="submit" value="Submit Application">
#         </div>
#     </form>
# </div>
#
# </body>
# </html>