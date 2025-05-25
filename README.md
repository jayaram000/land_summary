# 🗂️ Land Records Search & PDF Generator API

This Django-based REST API enables users to search land records by query (Parcel ID, Plot Number, or Owner Name) and generates a downloadable PDF report of matching results.

---

## 🚀 Features

- 🔍 Search land records via API (`/api/search/?query=value`)
- 📄 Generate dynamic PDF summary of search results
- 🧾 Simple HTML-to-PDF rendering using `xhtml2pdf`

---

## ⚙️ Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/your-username/land_summary.git
cd land_summary



 ## API Endpoint
GET /api/search/?query=value
Searches for land records and returns a PDF download of results.

### Approach



* Used Django and Django REST Framework (@api_view) to create a simple API endpoint.
* MySQL is used as the database
* Queried the Land model using icontains to allow partial matching on parcel_id, plot_number, and owner_name.
* Rendered an HTML template (summary.html) with matching results using render_to_string.
* Converted the rendered HTML into a PDF using xhtml2pdf.pisa.
* Returned the PDF as an HttpResponse with application/pdf MIME type.





