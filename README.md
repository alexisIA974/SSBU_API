# 🎮 SSBU Characters API

An unofficial REST API providing structured data for **Super Smash Bros. Ultimate** characters.

It includes competitive information such as archetypes, tier rankings, matchup tendencies, character attributes, stage preferences, and more. The API is designed to be lightweight, easy to use, and ideal for personal projects, dashboards, bots, or learning FastAPI.

> **Disclaimer**
>
> This project is **not affiliated with Nintendo** or the Super Smash Bros. Ultimate development team. It is a fan-made educational project.

---

# 📦 Installation

## Clone the repository

```bash
git clone https://github.com/alexisIA974/SSBU_API.git
cd SSBU_API
```

## Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install fastapi uvicorn
```

## Run the API

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🚀 Usage

Below are some of the available endpoints.

| Method | Endpoint | Description |
|:------:|----------|-------------|
| GET | `/character/{id}` | Returns a character by ID |
| GET | `/character/search/{name}` | Searches characters by name |
| GET | `/characters/filter` | Filter by `tier`, `archetype` or `difficulty` |
| GET | `/all_archetypes` | Lists every archetype |
| GET | `/tier-list` | Returns characters grouped by tier |
| GET | `/compare/{id1}/{id2}` | Compares two characters and indicates the expected winner |
| GET | `/matchup/{id}` | Returns a character’s matchup data (strong/weak against) |

Example:

```http
GET /character/1
```

Response:

```json
{
    "fighter_number": 1,
    "name": "Mario",
    "archetype": "All-Rounder",
    "tier": "A",
    ...
}
```

---

# 📂 Data

Each character contains competitive information including:

- Fighter number
- Archetype
- Tier
- Difficulty
- Signature moves
- Attributes
- Competitive tools
- Advantage state
- Disadvantage state
- Stage preferences
- Matchup tendencies

---

# 💻 Built With

- Python
- FastAPI
- Pydantic
- JSON

---

# 📖 Documentation

FastAPI automatically generates an OpenAPI specification.

Swagger UI:

```
/docs
```

ReDoc:

```
/redoc
```

---

# 📌 Roadmap

Planned improvements include:

- [ ] Better search & filters
- [ ] Improved matchup system  
- [ ] Statistics endpoints
- [ ] Add tests
- [ ] Database integration

---

# 🤝 Contributing

Suggestions and improvements are always welcome.

Feel free to open an issue or submit a pull request.

---

# 📄 License

This project is released under the MIT License.
