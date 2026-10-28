# 🛡️ Blockchain-Based Forensic Evidence Management System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-2.2%2B-092E20.svg?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Solidity](https://img.shields.io/badge/Solidity-%23363636.svg?logo=solidity&logoColor=white)](https://soliditylang.org/)
[![Web3.py](https://img.shields.io/badge/Web3.py-Ethereum-orange.svg?logo=ethereum&logoColor=white)](https://web3py.readthedocs.io/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1.svg?logo=mysql&logoColor=white)](https://www.mysql.com/)

A secure, tamper-proof, and decentralized forensic evidence management web application that leverages **Ethereum Smart Contracts** and **Django** to establish an immutable **Chain of Custody** for digital and physical evidence across legal and investigative proceedings.

---

## 📌 Problem Statement
In traditional criminal justice and forensic procedures, evidence records stored in centralized databases are susceptible to insider tampering, unauthorized modifications, accidental deletion, or broken chain of custody. Proving in court that evidence remained pristine from the crime scene to forensic analysis is often challenging.

## 💡 Solution
This system integrates a **private blockchain layer (Ethereum / Ganache)** with a **Full-Stack Django web application** and **MySQL**:
- Every critical evidence registration, custody transfer, and forensic report generation creates a cryptographically signed transaction stored on the blockchain.
- Data immutability guarantees that once evidence is recorded, it cannot be altered or fabricated.
- End-to-end chain of custody tracking provides transparent, audit-ready logs for law enforcement, forensics teams, and judicial bodies.

---

## 🚀 Key Features

- **🔗 Blockchain-Powered Immutability**:
  - Smart contracts written in **Solidity** store cryptographic records and audit trails directly on the Ethereum network.
  - Verifiable timestamps recorded via Ethereum block metadata (`block.timestamp`).
- **⛓️ End-to-End Chain of Custody Tracking**:
  - Complete chronological audit trails for every piece of evidence from initial seizure to courtroom presentation.
- **👥 Role-Based Access Control (RBAC)**:
  - **👮 Police Module**: Register crime details, log initial evidence, view status, and initiate evidence transfer requests.
  - **🔬 Forensic Module**: Receive evidence packets, perform scientific analysis, record examination findings, and log forensic reports directly to the blockchain.
  - **⚙️ Admin Module**: System configuration, manage authorized officers/laboratories, inspect audit trails, and oversee the integrity of the platform.
- **🔐 Dual-Layer Data Storage**:
  - Structured application data and user profiles managed efficiently in **MySQL**.
  - Immutable evidence hashes and audit records anchored directly to the **Ethereum Blockchain** via `Web3.py`.

---

## 🛠️ Tech Stack

| Domain | Technology / Tool |
|---|---|
| **Backend Framework** | Python 3, Django |
| **Blockchain & Smart Contracts** | Solidity (`Crime_SmartContract.sol`), Ganache, Web3.py |
| **Database** | MySQL, PyMySQL |
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap |
| **Development Tools** | VS Code, Git, GitHub |

---

## 📐 System Architecture

```text
+-------------------------------------------------------+
|                 Frontend Web Interface                |
|             (HTML5 / CSS3 / Bootstrap / JS)           |
+---------------------------+---------------------------+
                            |
                            v
+-------------------------------------------------------+
|                 Django Application Layer              |
|        [AdminApp]     [PoliceApp]     [ForensicApp]   |
+-------------+-----------------------------+-----------+
              |                             |
              v                             v
+---------------------------+ +-------------------------+
|    MySQL Relational DB    | |   Ethereum Blockchain   |
|   (Auth & Profile Data)   | |  (Solidity Smart Contr.)|
|       (PyMySQL)           | | (Web3.py Provider :9545)|
+---------------------------+ +-------------------------+
```

---

## ⚙️ Installation & Setup

### 1. Prerequisites
- Python 3.7+ installed
- MySQL Server installed and running
- Node.js & Ganache (for local blockchain node)
- Git

### 2. Clone Repository
```bash
git clone https://github.com/Premsai19/Block-chain-project.git
cd Block-chain-project
```

### 3. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 4. Database Setup
1. Open your MySQL client and create the database:
   ```sql
   CREATE DATABASE forensic_evidence;
   ```
2. Import the schema provided in `An impl/DATABASE/Database.sql`:
   ```bash
   mysql -u root -p forensic_evidence < "An impl/DATABASE/Database.sql"
   ```
3. Update your MySQL credentials in `An impl/SOURCE CODE/ForensicEvidence/Database.py` if different from `root`/`root`.

### 5. Blockchain Node & Smart Contract
1. Start Ganache or local Ethereum blockchain node on port `9545` (or `7545`/`8545` as configured in `PoliceApp/views.py`).
2. Deploy `Crime_SmartContract.sol` and ensure `Crime_SmartContract.json` and the deployed contract address are updated in the views.

### 6. Run the Django Server
```bash
cd "An impl/SOURCE CODE/ForensicEvidence"
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 📂 Project Structure

```text
├── An impl/
│   ├── BASEPAPER/          # Academic IEEE reference base paper
│   ├── DATABASE/           # MySQL database schema (Database.sql)
│   ├── DOCUMENT/           # Project abstract, presentations, and UML diagrams
│   └── SOURCE CODE/
│       └── ForensicEvidence/
│           ├── AdminApp/       # Administrative management views & controllers
│           ├── PoliceApp/      # Crime evidence logging & transfer requests
│           ├── ForensicApp/    # Forensic lab reports & verification
│           ├── ForensicEvidence/ # Django project settings & configuration
│           ├── Templates/      # UI HTML templates
│           ├── Static/         # CSS, JavaScript, and UI assets
│           ├── Crime_SmartContract.sol   # Solidity smart contract
│           ├── Crime_SmartContract.json  # Compiled contract ABI & bytecode
│           ├── Database.py     # MySQL database connector
│           └── manage.py       # Django CLI entrypoint
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Author
**Prem Sai Chithaluri**
- **GitHub**: [@Premsai19](https://github.com/Premsai19)
- **LinkedIn**: [Prem Sai Chithaluri](https://linkedin.com/in/premsai-chithaluri)
- **Email**: premsaichithaluri@gmail.com
