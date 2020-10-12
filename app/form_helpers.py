def get_form_from_request(request) -> dict:
    return request.form.to_dict()
