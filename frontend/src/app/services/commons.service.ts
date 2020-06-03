import { HttpHeaders } from '@angular/common/http';

export const baseurl = 'http://127.0.0.1:8000';
export const httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
};