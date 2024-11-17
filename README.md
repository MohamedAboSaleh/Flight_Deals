
# ✈️ Flight Deals  
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)  

**Flight Deals** is a Python-based project designed to help travelers and budget-conscious users find great flight deals. Using APIs and email notifications, it ensures users are informed of the best travel offers.  

---

## 📌 Features  
- 🌍 **Google Sheets Integration**: Manage city names, IATA codes, and target prices.  
- 🔍 **Flight Search**: Fetch flight deals via the [Tequila API](https://tequila.kiwi.com/portal/getting-started).  
- ✉️ **Email Alerts**: Notify users of deals using `smtplib`.  
- 📝 **User Management**: Add or remove users via a Google Sheet.  

---

## 📚 Project Workflow  

### 1️⃣ Manage Google Sheets  
We use the **Sheety API** to handle operations like `GET`, `POST`, and `PUT` to manage data efficiently.  

![Google Sheet Management](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/5e026fd5-55e5-446b-9909-e65a06b733e6)  

### 2️⃣ Search for Flights  
The **Tequila API** fetches flight deals for the next six months, starting from tomorrow's date. Searches are based on the target price in the Google Sheet.  

![Flight Search](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/e740155f-5881-40c7-a2da-cae92f190f86)  

### 3️⃣ Notify Users  
Once a deal is found, all users in the Google Sheet are notified via email. The `smtplib` library handles email sending.  

![Email Notification](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/4332f078-13d0-4f65-8318-abdb8ddadd85)  

---

## ⚙️ Setup Instructions  

### Prerequisites  
- **Python**: Version 3.10.3 or higher.  
- **API Keys**:  
  - [Sheety API](https://sheety.co): For Google Sheets management.  
  - [Tequila API](https://tequila.kiwi.com/portal/getting-started): For flight searches.  

### Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/MohamedAboSaleh/Flight_Deals.git
   cd Flight_Deals
   ```  
2. Add your API keys to the appropriate scripts:  


### Running the Project  
1. Update the Google Sheet with city names, IATA codes, and prices.  
2. Run the `users_main.py` script to add users:  
   ```bash
   python users_main.py
   ```  
3. Execute the main handler to find deals:  
   ```bash
   python flight_deals_handler/main.py
   ```  

---

## 🛠️ Technologies Used  
| Technology     | Purpose                             |  
|-----------------|-------------------------------------|  
| **Python**      | Core programming language          |  
| **Flask**       | Backend framework                  |  
| **Requests**    | API integration                    |  
| **smtplib**     | Sending email notifications        |  

---

## 🚧 Limitations  
- No GUI: Entirely script-based.  
- No user subscription management (e.g., unsubscribe).  

---

## 🎯 Future Plans  
This project was developed for educational purposes as part of the **"100 Days of Code"** Udemy course and is not planned for further updates.  


---

## 📷 Screenshots  

### Google Sheet Example  
![Google Sheet](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/5e026fd5-55e5-446b-9909-e65a06b733e6)  

### User Management Sheet  
![User Management](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/e740155f-5881-40c7-a2da-cae92f190f86)  

### Email Alert  
![Email Alert](https://github.com/MohamedAboSaleh/Flight_Deals/assets/135134225/4332f078-13d0-4f65-8318-abdb8ddadd85)  

---

Feel free to enhance this project and make it your own! Contributions are welcome. 😄  
