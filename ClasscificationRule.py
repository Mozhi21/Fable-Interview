class PersonClassifier:
    def __init__(self, classification_rules) -> None:
        self.classification_rules = classification_rules

    def classify_people(self, people:list) -> dict:
        category_to_people = {category: [] for category in self.classification_rules}
        
        for person in people:
            for category in self.classification_rules:
                if self._does_person_match_category(person, category):
                    category_to_people[category].append(person["id"])
        
        return category_to_people

    # helper functions:
    def _does_person_match_category(self, person, category) -> bool:
        methods = self.classification_rules[category]["methods"]
        for method in methods:
            var_value = person.get(method["var_name"])
            if not self._apply_comparator(var_value, method["comparator"], method["value"]):
                return False
        return True

    def _apply_comparator(self, var_value, comparator, expected_value):
        if comparator == "equal":
            return var_value == expected_value
        elif comparator == "in":
            return var_value in expected_value
        return False


test_classicification_rules = {
    "developer": {
        "methods": [
            {"var_name": "job_type", "comparator": "equal", "value": "developer"}
        ]
    },
    "QA_group": {
        "methods": [
            {"var_name": "related_field", "comparator": "equal", "value": "QA"}
        ]
    },
    "NY_developer": {
        "methods": [
            {"var_name": "job_type", "comparator": "equal", "value": "developer"},
            {"var_name": "location", "comparator": "in", "value": ["new_york", "NY", "New York"]}
        ]
    }
}

test_people = [
    {"id": 1, "name": "Alice", "job_type": "developer", "location": "NY", "related_field": "feature"},
    {"id": 2, "name": "Bob", "job_type": "developer", "location": "California", "related_field": "feature"},
    {"id": 3, "name": "Charlie", "related_field": "QA", "location": "New York", "job_type": "feature"},
    {"id": 4, "name": "David", "job_type": "designer", "location": "NY", "related_field": "back-end"},
    {"id": 5, "name": "Eve", "job_type": "developer", "location": "new_york", "related_field": "back-end"}
]

if __name__ == "__main__":
    test_classifier =PersonClassifier(test_classicification_rules)
    categories = test_classifier.classify_people(test_people)
    print(categories)