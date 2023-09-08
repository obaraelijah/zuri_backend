from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.views import APIView

class RetrieveApi(APIView):
    def get(self, request):
        slack_name = request.GET.get("slack_name")
        track = request.GET.get("track")

        data = {
            "slack_name": slack_name,
            "current_day": datetime.now().strftime('%A'),
            "utc_time": (datetime.utcnow() + timedelta(hours=0)).strftime('%Y-%m-%dT%H:%M:%SZ'),
            "track": track,
            "github_file_url": "https://github.com/obaraelijah/zuri_backend/blob/main/api/views.py",
            "github_repo_url": "https://github.com/obaraelijah/zuri_backend/tree/main",
            "status_code": 200
        }
        return Response(data)