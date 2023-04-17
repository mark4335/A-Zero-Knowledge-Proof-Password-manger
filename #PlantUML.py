#PlantUML
@startuml

class PasswordManager {
  +generate_response(challenge, salt, password_rules, commitment, master_key, password_manager_private_key)
  +verify_response(response, challenge, password_manager_public_key_bytes, salt, password_rules, commitment)
  -generate_random_salt()
  -generate_random_master_key()
}

class PasswordRules {
  -min_length: int
  -require_uppercase: bool
  -require_lowercase: bool
  -require_numbers: bool
  -require_symbols: bool
}

class User {
  +send_challenge(challenge)
  +verify_response(response, password_manager_public_key_bytes, salt, password_rules, commitment)
}

class Commitment {
  -salt: bytes
  -hash: bytes
}

class Challenge {
  -public_key: bytes
}

class Response {
  -encrypted_master_key: bytes
  -encrypted_commitment: bytes
}

PasswordManager -> PasswordRules
PasswordManager -> Commitment
PasswordManager -> Challenge
PasswordManager -> Response

User -> Challenge
User -> Response

Commitment -> PasswordManager

Challenge -> PasswordManager

Response -> PasswordManager

@enduml
