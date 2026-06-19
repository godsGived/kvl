import os

class MetricsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.total_requests = 0
        self.status_2xx = 0
        self.status_4xx = 0
        self.status_5xx = 0

    def __call__(self, request):
        response = self.get_response(request)
        
        self.total_requests += 1
        status_code = response.status_code
        
        if 200 <= status_code < 300:
            self.status_2xx += 1
        elif 400 <= status_code < 500:
            self.status_4xx += 1
        elif 500 <= status_code < 600:
            self.status_5xx += 1

        self._log_metrics()
        
        return response

    def _log_metrics(self):
        log_string = f"Total: {self.total_requests} | 2xx: {self.status_2xx} | 4xx: {self.status_4xx} | 5xx: {self.status_5xx}"
        
        print(f"=== {log_string} ===")
        
        with open("metrics.log", "w", encoding="utf-8") as f:
            f.write(log_string + "\n")