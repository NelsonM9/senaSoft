import { Injectable, } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class ClientService {

  constructor(private http: HttpClient) { }
  // tslint:disable-next-line: typedef
  getRequest(route: string, idu?: string, token?: string ) {
    console.log(idu)
    const config: any = {
      responseType: 'json',
    };

    if (idu){
      const params1 = new HttpParams().set('idu', idu);
      console.log(params1)
      config.params = params1
    }

    if (token) {
      const header = new HttpHeaders().set('Authorizaton', `Bearer${token}`);
      config.headers = header;
    }

    console.log(config);
    return this.http.get(route, config);
  }
  // tslint:disable-next-line: typedef
  postRequest(route: string, data?: any, token?: string) {
    const config: any = {
      responseType: 'json'
    };
    if (token) {
      const header = new HttpHeaders().set('Authorizaton', `Bearer${token}`);
      config.headers = header;
    }
    console.log(config);
    return this.http.post(route, data, config);
  }
  // tslint:disable-next-line: typedef
  deleteRequest(route: string, token?: string) {
    const config: any = {
      responseType: 'json'
    };
    if (token) {
      const header = new HttpHeaders().set('Authorizaton', `Bearer${token}`);
      config.headers = header;
    }
    console.log(config);
    return this.http.delete(route, config);
  }
  // tslint:disable-next-line: typedef
  putRequest(route: string, data?: string, token?: string) {
    const config: any = {
      responseType: 'json'
    };
    if (token) {
      const header = new HttpHeaders().set('Authorizaton', `Bearer${token}`);
      config.headers = header;
    }
    console.log(config);
    return this.http.put(route, data, config);
  }
}
