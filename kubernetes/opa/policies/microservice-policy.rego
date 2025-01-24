package microservice.policy

default allow = false

allow {
    input.method == "POST"
    input.path == "/create-order"
    input.user == "authorized-user"
}
