import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ClientService } from '../../client.service';

@Component({
  selector: 'app-appointments',
  templateUrl: './appointments.component.html',
  styleUrls: ['./appointments.component.css']
})
export class AppointmentsComponent implements OnInit {

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
  headers = ["Fecha", "Id Cita", "Id Doctor", "Id Paciente", "Razon", "Generar Cita"];
  rows = [];

  ngOnInit(): void {
    this.form = this.fb.group({
      reason: ['', Validators.required],
      id_p: ['', Validators.required],
      date_a: ['', Validators.required]
    });
  }

  async onSubmit() {
    if (this.form.valid) {
      setTimeout( () =>{
        this.rows = [];
        this.client.postRequest('http://127.0.0.1:5000/appointment', {
          reason: this.form.value.reason,
          id_p: this.form.value.id_p,
          date_a: this.form.value.date_a,
          id_a: '14',
          id_d: '1096145365'
        }).subscribe((response: any) => {
          this.dataEx = response;
          for (var j in this.dataEx['appointments']) {
            this.rows.push(this.dataEx['appointments'][j]);
          }
          console.log(response);
          this.form.reset();
        }),
          this.client.getRequest('http://127.0.0.1:5000/appointment',
            this.form.value.id_p
          ).subscribe((response: any) => {
            this.dataEx = response;
            console.log(this.dataEx)
            for (var i in this.dataEx) {
              for (var j in this.dataEx[i]) {
                this.rows.push(this.dataEx[i][j]);
              }
            }
            this.tabla()
            this.form.reset();
          }),
          (error) => {
            console.log(error.status);
            this.route.navigate(['/patient'])
          };
      }, 4000)
    } else {
      console.log('Error en la entrada de datos del formulario del cliente');
      this.notification = true;
    }
  }

  async addCita(appointment: any, id_row: number) {
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
