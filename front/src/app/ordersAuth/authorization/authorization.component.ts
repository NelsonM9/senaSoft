import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ClientService } from '../../client.service';
import { NgxFileDropEntry, FileSystemFileEntry, FileSystemDirectoryEntry } from 'ngx-file-drop';

@Component({
  selector: 'app-authorization',
  templateUrl: './authorization.component.html',
  styleUrls: ['./authorization.component.css']
})
export class AuthorizationComponent implements OnInit {

  form: FormGroup;
  form1: FormGroup;

  constructor(
    private fb: FormBuilder,
    private client: ClientService,
    private route: Router
  ) { }

  estado: boolean = false;
  tabla() {
    this.estado = true;
  }

  hide: true;
  notification: boolean;
  dataEx: JSON;
  state: string;
  headers = ["Id Orden", "Id Cita", "Diagnostico", "Generar Autorizacion"];
  rows = [];

  ngOnInit(): void {
    this.form = this.fb.group({
      id_p: ['', Validators.required]
    });
    this.form1 = this.fb.group({
      file_a: ['', Validators.required]
    })
  }
  async onSubmit() {
    if (this.form.valid) {
      this.rows = [];
      this.client.getRequest('http://127.0.0.1:5000/order', this.form.value.id_p).subscribe((response: any) => {
        this.dataEx = response;
        for (var j in this.dataEx['orders']) {
          this.rows.push(this.dataEx['orders'][j]);
          console.log('j', j);
        }
        this.tabla()
        this.form.reset();
      }),
        (error) => {
          console.log(error.status);
          this.route.navigate(['/patient'])
        };
    } else {
      console.log('Error en la entrada de datos del formulario del cliente');
      this.notification = true;
    }

  }

  async addAuthorization(order: any, id_row: number) {
    console.log('hola')
    this.client.postRequest('http://127.0.0.1:5000/authorization', {
      file_a: this.form1.value.file_a,
      id_auth: '1',
      id_o: this.rows[id_row]['id_o']
    }).subscribe((response: any) => {
      this.dataEx = response;
      this.state = this.dataEx['st'];
      switch (this.state) {
        case 'ok':
          if (order['id_o'] == this.rows[id_row]['id_o']) {
            this.rows.splice(id_row, 1);
            this.tabla()
            this.form1.reset();
          }
          console.log('agregado')
          break;
        case 'nothing': {
          console.log('Unregistred user')
          break;
        }
        case 'error': {
          console.log('error')
        }
      }
    });
  }

}
