import { HttpHeaders } from '@angular/common/http';

function getHttpOptionsWithAuth() {
    const accessToken = localStorage.getItem('accessToken');
    const headerWithToken = httpOptions['headers'].append('Authorization', `Bearer ${accessToken}`);
    const httpOptionsWithAuth = {
        headers: headerWithToken,
    }
    return httpOptionsWithAuth;
}

export const baseurl = 'http://127.0.0.1:8000';
export const httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
};
export { getHttpOptionsWithAuth as getHttpOptionsWithAuth }