"""
Disease information database
"""

disease_info = {
    "Bacterial Spot": {
        "scientific_name": "Xanthomonas campestris pv. vesicatoria",
        "type": "Bacterial disease",
        "symptoms": "Small, dark brown to black, greasy-looking spots on leaves with yellow halos. Spots may coalesce, causing leaf yellowing and drop.",
        "interventions": """
        <strong>Cultural Control:</strong>
        - Use certified disease-free seeds and transplants
        - Remove infected leaves immediately
        - Avoid overhead irrigation
        - Rotate crops with non-host plants

        <strong>Chemical Control:</strong>
        - Apply copper-based bactericides at first sign of disease
        - Use streptomycin sulfate for severe infections
        """,
        "severity": "Medium"
    },
    "Early Blight": {
        "scientific_name": "Alternaria solani",
        "type": "Fungal disease",
        "symptoms": "Dark brown to black concentric rings (target spots) on older leaves with yellow halos around lesions, leading to leaf drop.",
        "interventions": """
        <strong>Cultural Control:</strong>
        - Remove infected plant debris after harvest
        - Rotate crops with non-solanaceous plants for 2-3 years
        - Space plants for good air circulation
        - Water at soil level, avoid wetting foliage

        <strong>Chemical Control:</strong>
        - Apply chlorothalonil or mancozeb preventively
        - Use azoxystrobin for curative treatment
        """,
        "severity": "High"
    },
    "Late Blight": {
        "scientific_name": "Phytophthora infestans",
        "type": "Oomycete (fungus-like pathogen)",
        "symptoms": "Large, irregular, water-soaked spots on leaves that turn dark brown/black. Rapid leaf collapse and plant death in severe cases.",
        "interventions": """
        <strong>Cultural Control:</strong>
        - Use certified disease-free transplants
        - Remove and destroy infected plants immediately
        - Avoid cull piles near production fields
        - Ensure good air circulation

        <strong>Chemical Control:</strong>
        - Apply chlorothalonil or mancozeb preventively
        - Use mefenoxam or dimethomorph for active infections
        - Spray every 5-7 days during favorable conditions
        """,
        "severity": "Very High"
    },
    "Leaf Mold": {
        "scientific_name": "Passalora fulva",
        "type": "Fungal disease",
        "symptoms": "Pale green to yellow spots on upper leaf surface with olive-green to grayish-purple fuzzy mold growth on undersides.",
        "interventions": """
        <strong>Cultural Control:</strong>
        - Maintain low humidity and good ventilation
        - Avoid overhead irrigation
        - Remove and destroy affected leaves
        - Space plants adequately

        <strong>Chemical Control:</strong>
        - Apply chlorothalonil or mancozeb
        - Use azoxystrobin or boscalid for severe cases
        """,
        "severity": "Medium"
    },
    "Septoria Leaf Spot": {
        "scientific_name": "Septoria lycopersici",
        "type": "Fungal disease",
        "symptoms": "Small, circular spots (2-3 mm) with dark brown borders and tan centers. Multiple spots cause leaves to turn yellow and drop.",
        "interventions": """
        <strong>Cultural Control:</strong>
        - Remove and destroy infected leaves
        - Rotate crops with non-solanaceous plants
        - Avoid working in fields when wet
        - Use drip irrigation

        <strong>Chemical Control:</strong>
        - Apply chlorothalonil preventively
        - Use azoxystrobin for active infections
        """,
        "severity": "Medium"
    },
    "Two-Spotted Spider Mite": {
        "scientific_name": "Tetranychus urticae",
        "type": "Mite (arthropod pest)",
        "symptoms": "Tiny yellow or white speckling on upper leaf surface. Fine webbing on undersides of leaves, especially when populations are high.",
        "interventions": """
        <strong>Cultural Control:</strong>
        - Maintain adequate irrigation and humidity
        - Avoid water stress on plants
        - Remove weeds that host mites
        - Release predatory mites (Phytoseiulus persimilis)

        <strong>Chemical Control:</strong>
        - Avoid broad-spectrum insecticides that kill beneficials
        - Use selective miticides like abamectin or spiromesifen
        """,
        "severity": "Medium"
    },
    "Target Spot": {
        "scientific_name": "Corynespora cassiicola",
        "type": "Fungal disease",
        "symptoms": "Circular or irregular brown lesions with concentric rings (target pattern). Severely affected leaves turn yellow and drop.",
        "interventions": """
        <strong>Cultural Control:</strong>
        - Avoid overhead irrigation and wet foliage
        - Improve air circulation through pruning
        - Remove infected plant material
        - Rotate with non-host crops

        <strong>Chemical Control:</strong>
        - Apply chlorothalonil preventively
        - Use strobilurin fungicides for control
        """,
        "severity": "Medium"
    },
    "Tomato Yellow Leaf Curl Virus": {
        "scientific_name": "Tomato yellow leaf curl virus (TYLCV)",
        "type": "Viral disease",
        "symptoms": "Severe stunting with small, upward-curling leaves that turn yellow. Reduced leaf size and interveinal chlorosis.",
        "interventions": """
        <strong>Cultural Control:</strong>
        - Remove and destroy infected plants immediately
        - Control whitefly vector populations
        - Use virus-free seedlings
        - Install yellow sticky traps for monitoring

        <strong>Chemical Control:</strong>
        - Apply insecticides to control whiteflies (imidacloprid, pyriproxyfen)
        - Use reflective mulches to deter whiteflies
        """,
        "severity": "Very High"
    },
    "Tomato Mosaic Virus": {
        "scientific_name": "Tomato mosaic virus (ToMV)",
        "type": "Viral disease",
        "symptoms": "Light and dark green mottling ('mosaic') on leaves. Leaves may be distorted, fern-like, or smaller than normal.",
        "interventions": """
        <strong>Cultural Control:</strong>
        - Use certified virus-free seeds and transplants
        - Disinfect tools and hands after handling infected plants
        - Avoid tobacco use when handling tomatoes
        - Remove infected plants

        <strong>Chemical Control:</strong>
        - No chemical cure for virus
        - Focus on prevention and cultural control
        """,
        "severity": "High"
    },
    "Healthy Plant": {
        "scientific_name": "No pathogen detected",
        "type": "Healthy",
        "symptoms": "No visible disease symptoms. Leaves are uniform green color with normal growth pattern.",
        "interventions": """
        <strong>Preventive Care:</strong>
        - Maintain proper watering (avoid overwatering)
        - Provide adequate nutrition and fertilization
        - Ensure good soil drainage
        - Monitor plants regularly for early signs of stress

        <strong>Best Practices:</strong>
        - Practice crop rotation
        - Maintain garden hygiene
        - Use clean tools and equipment
        """,
        "severity": "None"
    }
}
