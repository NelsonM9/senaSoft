import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ClientService } from '../../client.service';
import { ToastrService } from 'ngx-toastr'

@Component({
  selector: 'app-orders',
  templateUrl: './orders.component.html',
  styleUrls: ['./orders.component.css']
})
export class OrdersComponent implements OnInit {

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
  headers = ["Fecha", "Id Cita", "Id Doctor", "Id Paciente", "Razon", "Generar orden"];
  rows = [];

  ngOnInit(): void {
    this.form = this.fb.group({
      id_p: ['', Validators.required],

    });
    this.form1 = this.fb.group({
      diagnosis: ['', Validators.required]
    })
  }

  async onSubmit() {
    if (this.form.valid) {
      this.rows = [];
      this.client.getRequest('http://127.0.0.1:5000/appointment', this.form.value.id_p).subscribe((response: any) => {
        this.dataEx = response;
        for (var j in this.dataEx['appointments']) {
          this.rows.push(this.dataEx['appointments'][j]);
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

  async addOrden(appointment: any, id_row: number) {
    console.log('hola')
    this.client.postRequest('http://127.0.0.1:5000/order', {
      diagnosis: this.form1.value.diagnosis,
      id_o: '1',
      id_a: this.rows[id_row]['id_a']
    }).subscribe((response: any) => {
      this.dataEx = response;
      this.state = this.dataEx['st'];
      switch (this.state) {
        case 'ok':
          if (appointment['id_a'] == this.rows[id_row]['id_a']) {
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
