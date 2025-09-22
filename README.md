# 📘 Assignment: Object-Oriented Programming in Python

This repository contains solutions to two OOP-focused assignments:

1. **Design Your Own Class**
2. **Polymorphism Challenge**

---

## 🏗️ Assignment 1: Design Your Own Class

We created a **Smartphone class** that inherits from a **Device class**.

### Features:

* **Attributes:** brand, model, operating system, storage.
* **Methods:** power on/off, take photo, install app.
* **Constructor:** Initializes each object with unique values.
* **Inheritance:** `Smartphone` inherits from the base class `Device`.

### Example:

```python
phone1 = Smartphone("Apple", "iPhone 15", "iOS", "256GB")
phone1.power_on()
phone1.take_photo()
phone1.install_app("WhatsApp")
phone1.power_off()
```

---

## 🎭 Activity 2: Polymorphism Challenge

We explored **polymorphism** using different types of vehicles.

### Features:

* **Base class:** `Vehicle`
* **Subclasses:** `Car`, `Plane`, and `Boat`
* **Polymorphism:** Each class implements its own version of `move()`

### Example:

```python
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
```

### Output:

```
Driving 🚗
Flying ✈️
Sailing 🚤
```

---

## ▶️ How to Run

1. Make sure you have **Python 3** installed.
2. Save the code into a file, e.g., `class.py`.
3. Run the program:

   ```bash
   python class.py
   ```

---

## ✨ Key OOP Concepts Practiced

* **Classes & Objects**
* **Constructors (`__init__`)**
* **Attributes & Methods**
* **Inheritance**
* **Polymorphism**

---

## 📂 Files

* `class.py` - Contains Assignment 1.
* `polymorphism.py` - contains assignment 2.
* `README.md` → Documentation for the project.

---

