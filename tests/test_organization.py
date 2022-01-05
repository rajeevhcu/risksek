from .test_data import test_case
from . import app

auth_header = {
    "Content-Type": "application/json"
}


def test_get_org_list(app):
    with app.test_client() as client:
        data = test_case['case_1']
        resp = client.get(
            f'http://127.0.0.1:5000/getOrganizations?page_size={data["page_size"]}&page_number={data["page_number"]}',
            headers=auth_header)
        assert resp.status_code == 200
        assert len(resp.json) == data['page_size']