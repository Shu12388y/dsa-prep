## Introduction to working on CPU

This is introduction to working on CPU

### Modern CPU pipeline

- In order frontend
- Out of order backend
- In order retirement

---

- |Branch predict| ->
- |Fetch |Decode | Rename| ->
- |ROB read | Excute | ROB write| ->
- |Retire|

---

### Branch Prediction

- Intelligence guess
- Is there a branch coming up?
- Where does it go?
- WIll it be taken

---

### Frontend

- Read instruction bytes
- Decode them into internal micro-operations
- Rewrites them to avoid data hazard

---

### Backend
