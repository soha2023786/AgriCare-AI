from datetime import datetime
from typing import Dict

def fertilizer_recommendation(data: Dict):
    n, p, k, ph = data["nitrogen"], data["phosphorus"], data["potassium"], data["ph"]
    notes, nutrients = [], []
    for name, value in (("Nitrogen", n), ("Phosphorus", p), ("Potassium", k)):
        if value < 40:
            nutrients.append(name)
    if ph < 5.5:
        notes.append("Soil is acidic; consider a soil-test-guided liming plan.")
    elif ph > 7.5:
        notes.append("Soil is alkaline; check micronutrient availability.")
    else:
        notes.append("Measured pH is within a commonly suitable range for many crops.")
    if nutrients:
        notes.append("Low readings reported for: " + ", ".join(nutrients) + ".")
    else:
        notes.append("NPK readings are not below this app's simple screening threshold.")
    return {
        "crop": data["crop"], "soil_type": data["soil_type"],
        "assessment": "Screening estimate based on user-entered NPK and pH values.",
        "low_nutrients": nutrients,
        "recommendations": notes,
        "next_step": "Confirm with a local soil laboratory and follow crop-specific, region-specific fertilizer rates before application.",
        "disclaimer": "Not a laboratory diagnosis. No fertilizer quantity is prescribed because units, soil-test method, crop stage and local recommendations are not yet verified."
    }

def pest_demo_result(filename):
    return {
        "filename": filename,
        "status": "image_received",
        "prediction": None,
        "message": "Image upload is working. A trained pest-detection model has not been bundled, so this version does not claim to identify a pest.",
        "next_step": "Connect a validated YOLO/CNN model trained on labelled pest images to enable real predictions.",
        "supported_future_outputs": ["pest class", "confidence score", "bounding boxes", "recommended integrated pest management steps"]
    }

def market_prices(crop, market):
    # Clearly labelled sample data. Replace with a verified live mandi-data provider.
    today = datetime.now().strftime("%Y-%m-%d")
    samples = {
        "Tomato": [1800, 1950, 1720, 2050, 1980],
        "Rice": [2300, 2280, 2350, 2320, 2400],
        "Cotton": [6800, 6950, 6870, 7020, 7100],
        "Onion": [2200, 2100, 2250, 2180, 2320],
        "Maize": [2100, 2150, 2080, 2200, 2170]
    }
    values = samples.get(crop, [1800, 1850, 1780, 1900, 1880])
    return {
        "crop": crop, "market": market, "unit": "INR per quintal",
        "date_checked": today, "sample_prices": values,
        "latest_sample_price": values[-1],
        "source_status": "DEMO DATA — not live market prices",
        "notice": "Connect Agmarknet/eNAM or another authorised data source before using prices for a selling decision."
    }

def digital_twin(data):
    moisture = data["soil_moisture"]
    temp = data["temperature_c"]
    irrigation = data["irrigation_percent"]
    days = data["days"]
    # Illustrative rule-based scenario; not a calibrated crop-growth model.
    moisture_after = max(0, min(100, moisture + (irrigation - 100) * 0.12 * days - max(0, temp - 30) * 0.25 * days))
    risk = "Low"
    if moisture_after < 20 or temp > 38:
        risk = "High"
    elif moisture_after < 30 or temp > 34:
        risk = "Moderate"
    return {
        "crop": data["crop"], "area_acres": data["area_acres"],
        "simulation_days": days, "starting_moisture_percent": moisture,
        "irrigation_setting_percent": irrigation,
        "estimated_moisture_after_simulation": round(moisture_after, 1),
        "heat_stress_indicator": "Elevated" if temp > 35 else "Not elevated",
        "scenario_risk": risk,
        "model_type": "Illustrative rule-based simulation",
        "notice": "This is a demonstration scenario, not a scientifically validated digital twin or yield forecast."
    }

def farming_assistant(question, language):
    q = question.lower()
    if any(word in q for word in ["yellow", "పసుపు", "पीला"]):
        answer = {
            "English": "Yellow leaves can be caused by nutrient deficiency, overwatering, pests or disease. Check soil moisture and inspect both sides of the leaves; confirm with a local agronomist.",
            "Telugu": "ఆకులు పసుపు రంగులోకి మారడానికి పోషకాల లోపం, అధిక నీరు, పురుగులు లేదా వ్యాధులు కారణం కావచ్చు. నేల తేమను, ఆకుల రెండు వైపులా పరిశీలించండి.",
            "Hindi": "पत्तियों का पीला होना पोषक तत्वों की कमी, अधिक पानी, कीट या बीमारी के कारण हो सकता है। मिट्टी की नमी और पत्तियों के दोनों तरफ जाँच करें।"
        }.get(language, "Yellow leaves can have several causes. Check moisture, nutrients and pests.")
    elif any(word in q for word in ["water", "irrigation", "నీరు", "पानी"]):
        answer = {
            "English": "Check soil moisture near the root zone before irrigating. Avoid watering on a fixed schedule if soil is already wet.",
            "Telugu": "నీరు పెట్టే ముందు వేర్ల దగ్గర నేల తేమను పరిశీలించండి. నేల ఇప్పటికే తడిగా ఉంటే మళ్లీ నీరు పెట్టవద్దు.",
            "Hindi": "सिंचाई से पहले जड़ों के पास मिट्टी की नमी जाँचें। मिट्टी पहले से गीली हो तो तय समय के कारण अतिरिक्त पानी न दें।"
        }.get(language, "Check root-zone soil moisture before irrigation.")
    else:
        answer = "I can help with soil health, irrigation, crop symptoms and market information. Share the crop, location and observed issue for more relevant guidance."
    return {"language": language, "answer": answer, "notice": "General guidance only; verify important crop-treatment decisions with a qualified local agriculture expert."}

def dashboard_summary():
    return {
        "platform": "AgriCare AI",
        "modules": ["Zone Monitoring", "Disease Detection", "Predictive Analytics", "Smart Irrigation",
                    "AI Assistant", "Fertilizer Recommendation", "Pest Detection",
                    "Market Price Intelligence", "Multilingual Voice Assistant", "Farm Digital Twin"],
        "status": "API operational",
        "data_note": "Market prices and digital-twin simulation are demo implementations until connected to verified data and validated models."
    }

def disease_guidance(crop):
    return {"crop": crop, "guidance": "Inspect affected leaves, isolate severely affected plants where practical, avoid overhead watering when leaf disease is suspected, and seek local diagnosis. Image-based disease prediction requires your original trained model."}

def irrigation_advice(moisture):
    if moisture < 25:
        advice = "Soil moisture is low. Check root-zone moisture and crop stage; irrigation may be needed."
    elif moisture < 45:
        advice = "Soil moisture is moderate. Recheck conditions and weather before irrigating."
    else:
        advice = "Soil moisture is relatively high. Avoid unnecessary irrigation and monitor drainage."
    return {"soil_moisture_percent": moisture, "advice": advice}
